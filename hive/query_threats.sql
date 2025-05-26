USE threat_detection;

INSERT OVERWRITE TABLE detected_threats
SELECT
    regexp_extract(log_line, '\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b', 0) AS ip,
    CASE
        WHEN log_line LIKE '%Failed password%' THEN 'Failed password'
        WHEN log_line LIKE '%Invalid user%' THEN 'Invalid user'
        WHEN log_line LIKE '%unauthorized%' THEN 'Unauthorized access'
        WHEN log_line LIKE '%break-in attempt%' THEN 'Break-in attempt'
        ELSE 'Unknown'
    END AS threat_type,
    log_line
FROM raw_logs
WHERE
    log_line LIKE '%Failed password%' OR
    log_line LIKE '%Invalid user%' OR
    log_line LIKE '%unauthorized%' OR
    log_line LIKE '%break-in attempt%';
