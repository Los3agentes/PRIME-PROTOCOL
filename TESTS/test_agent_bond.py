import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_bond import validate

class AgentBondTests(unittest.TestCase):
    def test_baseline_validates(self):
        self.assertEqual(validate(ROOT),[])
    def test_tamper_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            dst=Path(tmp)/'PRIME-PROTOCOL'
            shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('__pycache__','.pytest_cache','*.pyc'))
            f=dst/'HARD-CORE/COMMUNICATION.md'
            f.write_text(f.read_text(encoding='utf-8')+'\nunauthorized change\n',encoding='utf-8')
            errors=validate(dst)
            self.assertTrue(any('HASH_MISMATCH' in error for error in errors))
    def test_missing_attribution_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            dst=Path(tmp)/'PRIME-PROTOCOL'
            shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('__pycache__','.pytest_cache','*.pyc'))
            f=dst/'AGENT-BOND/REPORTS/INIT-0001.json'
            r=json.loads(f.read_text(encoding='utf-8'))
            r['signature']=''
            f.write_text(json.dumps(r),encoding='utf-8')
            self.assertTrue(validate(dst))
    def test_soft_core_disabled_by_default(self):
        idx=json.loads((ROOT/'SOFT-CORE/INDEX.json').read_text(encoding='utf-8'))
        self.assertFalse(idx['enabled_by_default'])
        self.assertFalse(idx['modules'][0]['enabled_by_default'])

if __name__=='__main__':unittest.main()
