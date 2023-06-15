select  a.*, b.*
  from  (select  date,
                 uid,
                 logged_hrs,
                 extract(hour from start_time) as hour
           from schema.table1
          where building = 'MKE'
            and pt_date between date '2019-01-01' and date '2019-01-09'
        ) as a
     left join 
       (select  associate_uid as uid,
                date(substr(fcdate_utc, 1, 10)) as pt_date,
                learning_curve_level
          from tenure.learningcurve 
         where warehouse_id = 'MKE'
           and date(substr(fcdate_utc, 1, 10)) between date '2019-01-01' and date '2019-01-09'
        ) as b 
      on a.uid=b.uid and a.pt_date = b.pt_date