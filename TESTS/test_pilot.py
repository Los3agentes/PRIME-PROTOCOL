import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'PILOT'))
from communication_worker import normalize_request

class PilotCommunicationTests(unittest.TestCase):
    def test_resolves_report_hint(self):
        result=normalize_request('Necesitamos un reporte ejecutivo')
        self.assertEqual(result['domain_hint'],'report')
        self.assertEqual(result['certainty'],'INFERRED')
    def test_does_not_fabricate_intent(self):
        result=normalize_request('Algo comercial')
        self.assertEqual(result['domain_hint'],'unspecified')
    def test_rejects_blank_request(self):
        with self.assertRaises(ValueError): normalize_request('   ')

if __name__=='__main__': unittest.main()
