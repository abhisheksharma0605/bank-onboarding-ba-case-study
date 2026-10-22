-- SQLite dialect. One row represents one submitted request.
CREATE VIEW normalized AS SELECT source_id,trim(applicant_name) AS applicant_name,
lower(trim(email)) AS email,trim(branch_code) AS branch_code,upper(trim(consent)) AS consent,
submitted_date,valid_date(submitted_date) AS date_valid FROM staging;

CREATE TABLE assessed AS SELECT n.*,CASE
 WHEN applicant_name='' THEN 'MISSING_NAME'
 WHEN email NOT LIKE '%_@_%._%' OR email LIKE '% %' THEN 'INVALID_EMAIL'
 WHEN branch_code NOT IN (SELECT branch_code FROM branches) THEN 'UNKNOWN_BRANCH'
 WHEN consent<>'Y' THEN 'CONSENT_MISSING'
 WHEN date_valid=0 THEN 'INVALID_DATE'
 WHEN source_id<>(SELECT MIN(n2.source_id) FROM normalized n2 WHERE n2.email=n.email)
 THEN 'DUPLICATE_EMAIL'
 ELSE 'ACCEPTED' END AS outcome FROM normalized n;

CREATE TABLE target_cases AS SELECT source_id AS case_id,applicant_name,email,branch_code,
submitted_date,'READY_FOR_REVIEW' AS case_status FROM assessed WHERE outcome='ACCEPTED';
CREATE TABLE exception_queue AS SELECT source_id,branch_code,submitted_date,outcome AS reason
FROM assessed WHERE outcome<>'ACCEPTED';
