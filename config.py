import os

# set API key
API_KEY = os.getenv('API_KEY')

# set the metrics
SLUG = 'bitcoin'
# SLUG = 'ethereum'
# set datetime range for metrics correlation
FROM_DATE = '2022-11-01 00:00:00'
# set interval for metrics correlation
INTERVAL = '1d'
# set metrics correlation file path
METRICS_CORRELATION_FILE = 'metrics_correlation_data.csv'

# query data every hour
FIRST_QUERY_FROME_DATE = '2022-11-29 00:00:00'
# set interval for query data
QUERY_INTERVAL = '1h'
# set data file path
DATA_CSV_FILE = SLUG + '.csv'

# execute a Python script after every n minutes
N = 60


