CREATE EXTERNAL TABLE IF NOT EXISTS `parket_test_files`.`user_data` (
  `first_name` string,
  `last_name` string,
  `email` string,
  `gender` string,
  `cc` string,
  `birthdate` string,
  `salary` double,
  `title` string,
  `comments` string
)
PARTITIONED BY (
  `country` string,
  `registrationdttm_` timestamp,
  `id` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://parket-test-files/'
TBLPROPERTIES ('classification' = 'parquet');