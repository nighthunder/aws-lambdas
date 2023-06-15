/* only can be used with tables with partioning */

ALTER TABLE orders ADD
  PARTITION (dt = '2016-05-14', country = 'IN')
  PARTITION (dt = '2016-05-15', country = 'IN');