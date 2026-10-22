import csv,json,sqlite3
from pathlib import Path
from datetime import date,datetime,timezone
ROOT=Path(__file__).resolve().parent
def valid_date(v):
    try:return int(date.fromisoformat(v).isoformat()==v)
    except (ValueError,TypeError):return 0
def run(source=None):
    db=sqlite3.connect(':memory:');db.row_factory=sqlite3.Row
    db.create_function('valid_date',1,valid_date)
    db.execute('CREATE TABLE staging(source_id TEXT PRIMARY KEY,applicant_name TEXT,email TEXT,branch_code TEXT,consent TEXT,submitted_date TEXT)')
    db.execute('CREATE TABLE branches(branch_code TEXT PRIMARY KEY,branch_name TEXT)')
    with (ROOT/'data/branches.csv').open(newline='',encoding='utf-8') as f:
        db.executemany('INSERT INTO branches VALUES(?,?)',[tuple(r.values()) for r in csv.DictReader(f)])
    if source is None:
        with (ROOT/'data/source_requests.csv').open(newline='',encoding='utf-8') as f:source=list(csv.DictReader(f))
    fields=['source_id','applicant_name','email','branch_code','consent','submitted_date']
    db.executemany('INSERT INTO staging VALUES(?,?,?,?,?,?)',[tuple(r[k] for k in fields) for r in source])
    db.executescript((ROOT/'sql/transform.sql').read_text())
    return db
def export(db,query,path):
    c=db.execute(query)
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow([x[0] for x in c.description]);w.writerows(c)
def main():
    db=run();out=ROOT/'evidence';out.mkdir(exist_ok=True)
    expected={f'S{i:03}':'ACCEPTED' for i in range(1,7)}
    expected.update(S007='DUPLICATE_EMAIL',S008='UNKNOWN_BRANCH',S009='CONSENT_MISSING',
                    S010='INVALID_EMAIL',S011='MISSING_NAME',S012='INVALID_DATE')
    actual={r['source_id']:r['outcome'] for r in db.execute('SELECT source_id,outcome FROM assessed')}
    assert actual==expected
    totals=[db.execute('SELECT COUNT(*) FROM '+t).fetchone()[0] for t in ('staging','target_cases','exception_queue')]
    assert totals==[12,6,6]
    for t in ('target_cases','exception_queue','assessed'):export(db,'SELECT * FROM '+t+' ORDER BY 1',out/(t+'.csv'))
    export(db,"SELECT source_id,CASE WHEN date_valid=1 THEN submitted_date ELSE NULL END AS submitted_date,branch_code,outcome FROM assessed ORDER BY source_id",out/'fact_requests.csv')
    export(db,"SELECT * FROM branches UNION SELECT DISTINCT branch_code,'Unmapped branch' FROM assessed WHERE branch_code NOT IN (SELECT branch_code FROM branches) ORDER BY 1",out/'dim_branch.csv')
    queries=[q for q in (ROOT/'sql/reporting.sql').read_text().split(';') if q.strip()]
    reports=[[dict(r) for r in db.execute(q)] for q in queries]
    (out/'sql-reporting.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
    report=f"# Executed migration rehearsal\n\nRun UTC: {datetime.now(timezone.utc).isoformat()}\n\n"
    report+="**12 source requests = 6 accepted + 6 quarantined. Acceptance rate: 50%.**\n\n"
    report+="| Source | Expected | Actual | Result |\n|---|---|---|---|\n"
    report+='\n'.join(f'| {k} | {expected[k]} | {v} | PASS |' for k,v in actual.items())
    report+="\n\nAll fixture data checks passed. Business UAT and Power BI Desktop validation are pending. Release recommendation: **NO-GO**, because six exceptions remain unresolved and business acceptance has not occurred.\n"
    (out/'results.md').write_text(report,encoding='utf-8');db.close()
    print('PASS: 12 expected outcomes; 12 = 6 accepted + 6 exceptions; 3 SQL reports')
if __name__=='__main__':main()
