CREATE DATABASE threat_detection;
USE threat_detection;

CREATE EXTERNAL TABLE IF NOT EXISTS raw_logs (
    log_line STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION '/logs/raw';

CREATE TABLE IF NOT EXISTS detected_threats (
    ip STRING,
    threat_type STRING,
    log_line STRING
)
STORED AS TEXTFILE;
