"""PRIME local integrity gate. Structural consistency only; NOT cryptographic authorization."""
from __future__ import annotations
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED_CORE = ('COMMUNICATION','COGNITION','CREATIVITY','REFERENCES','EXECUTION','DELIVERABLES','CONTINUITY')
SKIP = {'AGENT-BOND/BOND_MANIFEST.json'}

def digest(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inventory(root:Path)->dict[str,str]:
    result={}
    for p in root.rglob('*'):
        if not p.is_file(): continue
        name=p.relative_to(root).as_posix()
        if name in SKIP or name.startswith(('.git/','__pycache__/','.pytest_cache/')) or '/__pycache__/' in name or name.endswith(('.pyc','.pyo')) or name=='.DS_Store': continue
        result[name]=digest(p)
    return result

def metadata(content:str)->dict[str,str]|None:
    match=re.search(r'<!-- PRIME_META\s*\n(.*?)\n-->',content,re.S)
    if not match:return None
    meta={}
    for line in match.group(1).splitlines():
        if ':' in line:
            key,value=line.split(':',1)
            meta[key.strip()]=value.strip()
    return meta

def validate(root:Path)->list[str]:
    errors=[]
    root=root.resolve()
    try: m=json.loads((root/'AGENT-BOND/BOND_MANIFEST.json').read_text(encoding='utf-8'))
    except (OSError,ValueError) as e:return [f'Cannot read BOND_MANIFEST: {e}']
    try: version=json.loads((root/'VERSION.json').read_text(encoding='utf-8'))['v']
    except (OSError,ValueError,KeyError) as e:return [f'Cannot read VERSION: {e}']
    if m.get('v')!=version:errors.append('Manifest version differs from VERSION.json')
    actual=inventory(root)
    expected=m.get('files',{})
    for name in sorted(set(expected)-set(actual)):errors.append(f'MISSING: {name}')
    for name in sorted(set(actual)-set(expected)):errors.append(f'UNTRACKED: {name}')
    for name in sorted(set(actual)&set(expected)):
        if actual[name]!=expected[name]:errors.append(f'HASH_MISMATCH: {name}')
    required={f'HARD-CORE/{s}.md' for s in REQUIRED_CORE}
    required.update(['SOFT-CORE/AUTONOMOUS_ACTION.md','SOFT-CORE/INDEX.json','AGENT-BOND/AGENT_BOND.md','PROJECTS/PRIME-PROTOCOL/CHANGELOG.csv','PILOT/communication_worker.py'])
    for name in sorted(required-set(actual)):errors.append(f'REQUIRED_MISSING: {name}')
    docs=m.get('protocols',{})
    for path,entry in docs.items():
        if path not in actual:errors.append(f'PROTOCOL_MISSING: {path}');continue
        try:meta=metadata((root/path).read_text(encoding='utf-8'))
        except (OSError,UnicodeDecodeError):meta=None
        if not meta:errors.append(f'META_MISSING: {path}');continue
        for key,want in [('id',entry.get('id')),('v',version),('A',str(entry.get('A'))),('core',entry.get('core'))]:
            if meta.get(key)!=want:errors.append(f'META_INVALID: {path}:{key} (expected {want!r})')
        if not meta.get('author_signature'):errors.append(f'ATTRIBUTION_MISSING: {path}')
    for path in actual:
        if path.endswith('.md') and path!='README.md' and path not in docs:
            errors.append(f'UNREGISTERED_PROTOCOL: {path}')
    try:
        idx=json.loads((root/'SOFT-CORE/INDEX.json').read_text(encoding='utf-8'))
        modules=idx['modules']; mod=next((q for q in modules if q['id']=='PP-SC-AUTONOMOUS-ACTION'),None)
        if not mod or mod.get('enabled_by_default') is not False or idx.get('default_policy')!='SELECTIVE':errors.append('Soft core not opt-in in index')
    except (OSError,ValueError,KeyError,TypeError) as e:errors.append(f'INVALID_SOFT_INDEX: {e}')
    try:
        log_path=root/'PROJECTS/PRIME-PROTOCOL/CHANGELOG.csv'
        with log_path.open(newline='',encoding='utf-8') as f:rows=list(csv.DictReader(f))
        if not rows: errors.append('EMPTY_CHANGELOG')
        if m.get('change_count')!=len(rows):errors.append('CHANGE_COUNT_MISMATCH')
        seen=set()
        for row in rows:
            ref=row.get('report_path','');cid=row.get('change_id','')
            if cid in seen:errors.append('DUPLICATE_CHANGE_ID: '+cid)
            seen.add(cid)
            if not (cid and ref and row.get('actor') and row.get('authorization_id') and row.get('signature')):errors.append('UNSIGNED_OR_INCOMPLETE_LOG: '+cid)
            rp=root/ref
            if not rp.is_file():errors.append('REPORT_MISSING: '+ref);continue
            report=json.loads(rp.read_text(encoding='utf-8'))
            if report.get('change_id')!=cid or report.get('actor')!=row.get('actor') or report.get('authorization_id')!=row.get('authorization_id') or report.get('signature')!=row.get('signature'):
                errors.append('REPORT_LOG_MISMATCH: '+cid)
            if not isinstance(report.get('changed_files'),list) or not report.get('changed_files') or not report.get('verification') or not report.get('reason'):
                errors.append('REPORT_INCOMPLETE: '+cid)
        if rows and rows[-1].get('v')!=version:errors.append('LATEST_VERSION_LOG_MISMATCH')
    except (OSError,ValueError,KeyError) as e:errors.append(f'INVALID_CHANGELOG_OR_REPORT: {e}')
    return errors

def main():
    root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
    errors=validate(root)
    if errors:
        for error in errors:print('FAIL',error)
        return 1
    print('PASS PRIME AGENT BOND: hashes, protocol metadata, soft activation, changelog and signed report records are consistent.')
    print('NOTE: signatures and authorization IDs are text attribution, not cryptographic identity proof.')
    return 0
if __name__=='__main__':sys.exit(main())
