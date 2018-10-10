mydatabase=> CREATE TABLE crawl (
mydatabase(>     id SERIAL NOT NULL PRIMARY KEY,
mydatabase(>     url VARCHAR(150) NOT NULL,
mydatabase(>     response JSON NOT NULL
mydatabase(> );
CREATE TABLE

mydatabase=> SELECT 
mydatabase->     id, --url,
mydatabase->     response_each ->> 'code' AS code,
mydatabase->     response_each ->> 'candleDateTime' AS candleDateTime,
mydatabase->     response_each ->> 'candleDateTimeKst' AS candleDateTimeKst,
mydatabase->     response_each ->> 'openingPrice' AS openingPrice,
mydatabase->     response_each ->> 'highPrice' AS highPrice,
mydatabase->     response_each ->> 'lowPrice' AS lowPrice,
mydatabase->     response_each ->> 'tradePrice' AS tradePrice,
mydatabase->     response_each ->> 'candleAccTradeVolume' AS candleAccTradeVolume,
mydatabase->     response_each ->> 'candleAccTradePrice' AS candleAccTradePrice,
mydatabase->     (response_each ->> 'timestamp') :: bigint AS timestamp,
mydatabase->     response_each ->> 'unit' AS unit
mydatabase-> FROM ( 
mydatabase(>     SELECT id, url, json_array_elements(response) AS response_each 
mydatabase(>     FROM crawl 
mydatabase(> ) AS a 
mydatabase-> ORDER BY
mydatabase->     id, timestamp
mydatabase-> ;
 id |        code        |      candledatetime       |     candledatetimekst     | openingprice | highprice | lowprice | tradeprice | candleacctradevolume | candleacctradeprice |   timestamp   | unit 
----+--------------------+---------------------------+---------------------------+--------------+-----------+----------+------------+----------------------+---------------------+---------------+------
  1 | CRIX.UPBIT.KRW-ETH | 2018-06-06T09:30:00+00:00 | 2018-06-06T18:30:00+09:00 | 660500.0     | 660500.0  | 658900.0 | 658900.0   | 117.3868824          | 77417565.561081     | 1528278000923 | 10
  1 | CRIX.UPBIT.KRW-ETH | 2018-06-06T09:40:00+00:00 | 2018-06-06T18:40:00+09:00 | 658900.0     | 658900.0  | 658300.0 | 658800.0   | 64.61783189          | 42556616.269565     | 1528278604397 | 10
  1 | CRIX.UPBIT.KRW-ETH | 2018-06-06T09:50:00+00:00 | 2018-06-06T18:50:00+09:00 | 658200.0     | 660400.0  | 657700.0 | 660300.0   | 87.97134155          | 57909398.695062     | 1528279171570 | 10
(3 rows)
