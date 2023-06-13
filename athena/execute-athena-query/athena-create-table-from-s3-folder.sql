/* View parquet files: https://www.parquet-viewer.com/ */

/* parket_test_files is the name of a s3 folder */

DROP TABLE IF EXISTS `parket_test_files`.`user_data`;
CREATE EXTERNAL TABLE IF NOT EXISTS `parket_test_files`.`user_data` (
  `registration_dttm` timestamp,
  `id` int,
  `first_name` string,
  `last_name` string,
  `email` string,
  `gender` string,
  `ip_address` string,
  `cc` string,
  `country` string,
  `birthdate` string,
  `salary` double,
  `title` string,
  `comments` string
) COMMENT "The user table log"
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://parket-test-files/'
TBLPROPERTIES ('classification' = 'parquet');