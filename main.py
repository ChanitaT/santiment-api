import san
import time
import pandas as pd
from datetime import datetime, timezone
from utils import utc_time, get_data
from config import (
    API_KEY, 
    SLUG,
    QUERY_INTERVAL,
    DATA_CSV_FILE,
    FIRST_QUERY_FROME_DATE,
    N
    )

#Configuratin api key
san.ApiConfig.api_key = API_KEY

def get_dataframe(metrics, slug, last_update, end_update, interval):
    df = pd.DataFrame()

    for metric in metrics:
        data = get_data(metric, slug, last_update, end_update, interval)
        if data.empty:
            print(f'{metric} is empty')
        else:
            temp_df = data.rename(columns = {'value': metric})
            print(f'{utc_time(0)}: {metric} is added')

            if df.empty:
                df = temp_df
            else:
                df = df.join(temp_df, on='datetime')
    return df

def main():
    # get good correlation metrics
    good_correlation_metrics = ['active_addresses_1h',
                                'dev_activity',
                                'dev_activity_contributors_count',
                                'github_activity',
                                'github_activity_contributors_count',
                                'volume_usd']

    # get the last datetime from csv file and update data
    end_update = utc_time(0)
    try:
        df = pd.read_csv(DATA_CSV_FILE, index_col=0)

    except FileNotFoundError: 
        df = get_dataframe(good_correlation_metrics, SLUG, FIRST_QUERY_FROME_DATE, end_update, QUERY_INTERVAL)
        df.to_csv(DATA_CSV_FILE)
        print(f'Initially saved successfully on {DATA_CSV_FILE}')

    last_update = df.index.values[-1]
    datetime_object = datetime.strptime(last_update, '%Y-%m-%d %H:%M:%S%z')
    update_on = datetime_object

    update_df = get_dataframe(good_correlation_metrics, SLUG, update_on, end_update, QUERY_INTERVAL)
    df.index = pd.to_datetime(df.index)
    update_df = pd.concat((df, update_df)).groupby('datetime').max()

    if update_df.empty:
        print("There is no data to update")
    else:
        update_df.to_csv(DATA_CSV_FILE)
        print(f'Data saved successfully on {DATA_CSV_FILE}')

if __name__ == '__main__':
    # execute a Python script after every N minutes
    milliseconds = N*60

    def job():
        print(datetime.now(timezone.utc))
        print("Running...")
        print(SLUG)
        print('---------------------------------------')
        main()

    while True:
        job()
        print(f"sleep for {N} minute(s)...")
        time.sleep(milliseconds)
    