# santiment-api
The script connecting Santiment API to save useful data series on csv file for any slugs every hour by
    running on the docker. 
    
There are 2 main python files.
* ``` main.py ``` to execute the script hourly and save data in csv file and
* ``` metrics.py ``` to calculate correlation of the metrics with the price

## How to configuration
In the cofig.py, you can set 
* Set the API key ``` API_KEY = 'YOUR_API_KEY' ```
* The slug name ``` SLUG = 'bitcoin' ```
* The date range to calculate metrics correlation with the price (USD) which calculate from *FROM_DATE* to today
``` FROM_DATE = '2022-01-01 00:00:00' ```
* The date range of data
``` FIRST_QUERY_FROME_DATE = '2022-11-29 00:00:00' ```
* The frequency of the data (5 minutes, 1 hour or 1 day etc.) 
``` INTERVAL = '1d' ```
``` QUERY_INTERVAL = '1h' ```
* How often to execute the script ``` N = 60 ```

## The metrics correlation
The script on ```metrics.py``` will calculate correlation based on **The Pearson correlation coefficient (r)** which is measures the strength and direction of the relationship between two variables.
* The first variable is Price of the slug in USD (*price_usd*)
* The secound variable is the avalible metrics
    All the metrics correlation is saved on "metrics_correlation_data.csv"

    After removing the metrics which retate to the price and sort by good positive and negative correlation.
    The metrics that have hourly data are selected.

## Collect data every hour
run the docker

```
sudo docker run --env-file .env -v ${PWD}:/app santiment-api
```
