import csv,sqlite3,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from run_case_study import ROOT,run
class MigrationTests(unittest.TestCase):
    def setUp(self):
        with (ROOT/'data/source_requests.csv').open(newline='',encoding='utf-8') as f:self.rows=list(csv.DictReader(f))
    def test_expected_counts(self):
        db=run(self.rows)
        self.assertEqual([db.execute('SELECT COUNT(*) FROM '+t).fetchone()[0] for t in ('staging','target_cases','exception_queue')],[12,6,6]);db.close()
    def test_normalized_duplicate(self):
        db=run(self.rows);self.assertEqual(db.execute("SELECT outcome FROM assessed WHERE source_id='S007'").fetchone()[0],'DUPLICATE_EMAIL');db.close()
    def test_duplicate_input_key_fails(self):
        with self.assertRaises(sqlite3.IntegrityError):run(self.rows+[self.rows[0]])
    def test_invalid_calendar_day(self):
        db=run([{**self.rows[0],'submitted_date':'2026-02-30'}])
        self.assertEqual(db.execute('SELECT outcome FROM assessed').fetchone()[0],'INVALID_DATE');db.close()
    def test_corrected_fixture(self):
        changes={'S007':{'email':'a07@example.invalid'},'S008':{'branch_code':'101'},
        'S009':{'consent':'Y'},'S010':{'email':'a10@example.invalid'},
        'S011':{'applicant_name':'Applicant 11'},'S012':{'submitted_date':'2026-09-06'}}
        db=run([{**r,**changes.get(r['source_id'],{})} for r in self.rows])
        self.assertEqual(db.execute('SELECT COUNT(*) FROM target_cases').fetchone()[0],12);db.close()
if __name__=='__main__':unittest.main()
