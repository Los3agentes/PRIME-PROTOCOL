"""Records authorized edits in a local structural manifest; not an approval authority."""
from __future__ import annotations
import argparse
import csv
from datetime import datetime,timezone
import json
from pathlib import Path
import re
import sys
from validate_bond import digest,inventory,metadata,validate

ROOT=Path(__file__).resolve().parents[1]
LOG_FIELDS=['change_id','date','actor','authorization_id','reason','v','changed_paths','report_path','signature']

def stamp(text:str,v:str|None=None,A:int|None=None,actor:str|None=None)->str:
    found=re.search(r'<!-- PRIME_META\s*\n(.*?)\n-->',text,re.S)
    if not found:raise ValueError('Missing PRIME_META')
    part=found.group(1)
    for key,value in [('v',v),('A',str(A) if A is not None else None),('author_signature',f'{actor} (attribution only)' if actor else None)]:
        if value is not None:
            part,n=re.subn(rf'(?m)^({re.escape(key)}:)\s*.*$',lambda m:m.group(1)+' '+value,part)
            if n!=1:raise ValueError('Invalid header '+key)
    return text[:found.start(1)]+part+text[found.end(1):]

def main(argv=None)->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',nargs='?',type=Path,default=ROOT)
    p.add_argument('--actor',required=True)
    p.add_argument('--authorization-id',required=True)
    p.add_argument('--reason',required=True)
    p.add_argument('--authorization-file',type=Path,help='optional JSON contract with allowed_paths and actor')
    p.add_argument('--judge-version',help='new v requiring JUEZ approval ref')
    p.add_argument('--judge-approval',help='explicit reference to approval by JUEZ')
    args=p.parse_args(argv)
    root=args.root.resolve()
    manifest_path=root/'AGENT-BOND/BOND_MANIFEST.json'
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    current_version=manifest['v']
    if args.judge_version and (not args.judge_approval or args.judge_version==current_version):
        print('FAIL --judge-version requires a new version and --judge-approval reference');return 1
    if args.judge_approval and not args.judge_version:
        print('FAIL --judge-approval requires --judge-version');return 1
    version=json.loads((root/'VERSION.json').read_text(encoding='utf-8'))
    if version['v']!=current_version and not args.judge_version:
        print('FAIL VERSION.json edited without declared JUEZ authorization');return 1
    before=manifest['files']
    present=inventory(root)
    removed=set(before)-set(present)
    if removed:
        print('FAIL deleted managed files require manual JUEZ-controlled procedure:',sorted(removed));return 1
    changed=sorted(x for x in present if present[x]!=before.get(x))
    tracked_proto=set(manifest['protocols'])
    for path in changed:
        if path in tracked_proto:
            meta=metadata((root/path).read_text(encoding='utf-8'))
            if not meta or meta.get('v')!=current_version or str(meta.get('A'))!=str(manifest['protocols'][path]['A']):
                print('FAIL protocol metadata edited without authority or not based on previous A:',path);return 1
    if args.authorization_file:
        contract=json.loads(args.authorization_file.read_text(encoding='utf-8'))
        paths=set(contract.get('allowed_paths',[]))
        if not paths or contract.get('actor')!=args.actor or contract.get('authorization_id')!=args.authorization_id:
            print('FAIL invalid authorization contract');return 1
        forbidden=[x for x in changed if x not in paths]
        if forbidden:
            print('FAIL files outside authorization allowlist:',forbidden);return 1
    if not changed and not args.judge_version:
        print('FAIL no content changes to record');return 1
    if args.judge_version:
        version['v']=args.judge_version
        (root/'VERSION.json').write_text(json.dumps(version,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        for name in tracked_proto:
            file=root/name
            file.write_text(stamp(file.read_text(encoding='utf-8'),v=args.judge_version,actor=args.actor),encoding='utf-8')
        manifest['v']=args.judge_version
    for name in tracked_proto:
        if name in changed:
            file=root/name
            newA=int(manifest['protocols'][name]['A'])+1
            file.write_text(stamp(file.read_text(encoding='utf-8'),A=newA,actor=args.actor),encoding='utf-8')
            manifest['protocols'][name]['A']=newA
    # New Markdown protocols must first be registered by a controlled JUEZ procedure.
    extra_protos=[x for x in changed if x.endswith('.md') and x not in tracked_proto and x!='README.md']
    if extra_protos:
        print('FAIL cannot auto-register protocol:',extra_protos);return 1
    changed=sorted(set(changed)|({ 'VERSION.json'} if args.judge_version else set())|(tracked_proto if args.judge_version else set()))
    actual=inventory(root)
    change_count=manifest['change_count']+1
    cid=f'CHG-{change_count:04d}'
    now=datetime.now(timezone.utc).isoformat(timespec='seconds')
    signature=f'{args.actor}: declarative attribution / {args.authorization_id}'
    report_path=f'AGENT-BOND/REPORTS/{cid}.json'
    report={'change_id':cid,'date':now,'actor':args.actor,'authorization_id':args.authorization_id,'reason':args.reason,
            'signature':signature,'version_before':current_version,'version_after':manifest['v'],
            'version_approval':args.judge_approval,'verification':['local structural bond validation; independent tests run separately'],
            'changed_files':[{'path':path,'sha256':actual[path]} for path in changed]}
    report_file=root/report_path;report_file.parent.mkdir(parents=True,exist_ok=True)
    report_file.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    log_file=root/'PROJECTS/PRIME-PROTOCOL/CHANGELOG.csv'
    with log_file.open('a',newline='',encoding='utf-8') as file:
        w=csv.DictWriter(file,fieldnames=LOG_FIELDS)
        w.writerow({'change_id':cid,'date':now,'actor':args.actor,'authorization_id':args.authorization_id,'reason':args.reason,
                    'v':manifest['v'],'changed_paths':';'.join(changed),'report_path':report_path,'signature':signature})
    manifest['change_count']=change_count
    manifest['files']=inventory(root)
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    errors=validate(root)
    if errors:
        print('FAIL generated changeset did not validate:')
        print('\n'.join(errors));return 1
    print('PASS recorded',cid,'changed',len(changed),'version',manifest['v'])
    return 0
if __name__=='__main__':sys.exit(main())
