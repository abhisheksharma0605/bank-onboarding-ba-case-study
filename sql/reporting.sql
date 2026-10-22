SELECT COUNT(*) AS source_count,
SUM(CASE WHEN outcome='ACCEPTED' THEN 1 ELSE 0 END) AS accepted,
SUM(CASE WHEN outcome<>'ACCEPTED' THEN 1 ELSE 0 END) AS exceptions,
ROUND(100.0*SUM(CASE WHEN outcome='ACCEPTED' THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0),2) AS acceptance_percent
FROM assessed;

SELECT outcome,COUNT(*) AS requests FROM assessed GROUP BY outcome;

-- LEFT JOIN retains the unknown branch. It must not disappear from a report.
SELECT COALESCE(b.branch_name,'Unmapped branch') AS branch,COUNT(*) AS requests,
SUM(CASE WHEN a.outcome='ACCEPTED' THEN 1 ELSE 0 END) AS accepted
FROM assessed a LEFT JOIN branches b ON a.branch_code=b.branch_code
GROUP BY COALESCE(b.branch_name,'Unmapped branch');
