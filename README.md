# santiment-api
The script connecting Santiment API to save useful data series on csv file for any slugs every hour by
    running on the docker.
By running ``` main.py ``` to execute the script hourly and save data in csv file and
runnung ``` metrics.py ``` to calculate correlation of the metrics with the price

## How to configuration
In the cofig.py, you can set 
* Set the API key
``` API_KEY = 'YOUR_API_KEY' ```
* The slug name 
``` SLUG = 'bitcoin' ```
* The date range to calculate metrics correlation with the price (USD) which calculate from *FROM_DATE* to today
``` FROM_DATE = '2022-01-01 00:00:00' ```
* The date range of data
``` FIRST_QUERY_FROME_DATE = '2022-11-29 00:00:00' ```
* The frequency of the data (5 minutes, 1 hour or 1 day etc.) 
``` INTERVAL = '1d' ```
``` QUERY_INTERVAL = '1h' ```
* How often to execute the script
``` N = 60 ```

## How the metrics correlation works?
1. Select all avalible metrics
1. Select metrics which is free subscription (no error)
1. Select good correlation metrics with price and there is an hour frequency data
    this selecting metrics based on The Pearson correlation coefficient (r) which is measures the strength and direction of the relationship between two variables.
        - The first variable is Price of the slug in USD (price_usd)
        - The secound variable is the metrics that avalible with 2nd step
    All the metrics correlation is saved on "metrics_correlation_data.csv"

    After removing the metrics relatated to the price and sort by good correlation both positive and negative as example data below.
    	| metric | correlation | pvalue |
        | --- | --- | --- |
        | active_addresses_24h_change_30d | -0.859841 |	1.149394e-09 |
        | active_addresses_30d | -0.834351 | 1.010246e-08 |
        | circulation |	-0.786530 | 2.565085e-07 |
        | mcd_erc20_supply | -0.786530 | 2.565085e-07 |
        | total_supply | -0.786530 | 2.565085e-07 |
        | twitter_followers | -0.759261 | 1.148887e-06 |
        | active_addresses_7d |	-0.649374 |	1.033205e-04 |
        | 30d_moving_avg_dev_activity_change_1d |	0.477379 |	7.638776e-03 |
        | volume_usd |	0.275461 |	1.406621e-01 |
        | volume_usd_change_7d |	0.249794 |	1.831037e-01 |
        | ... | ... | ... |

    The metrics from the table that have hourly data are selected.

## Collect data every hour
run the docker

```
sudo docker run --env-file .env -v ${PWD}:/app santiment-api
```
