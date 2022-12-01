import san
from scipy.stats import pearsonr
import pandas as pd
from utils import utc_time, get_data
from config import (
    SLUG, 
    FROM_DATE, 
    INTERVAL, 
    METRICS_CORRELATION_FILE
)

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def get_metrics(slug):
    metrics = san.available_metrics_for_slug(slug)
    return metrics

def main():
    # get all metrics
    all_metrics = get_metrics(SLUG)

    # query data with free subscription metrics and calculate correlation
    correlation_df = pd.DataFrame(columns=['metric', 'correlation', 'pvalue'])
    now = utc_time(0)
    price = get_data('price_usd', SLUG, FROM_DATE, now, INTERVAL)
    price = price.rename(columns = {'value': 'price_usd'})

    for metric in all_metrics:
        
        try: 
            data = get_data(metric, SLUG, FROM_DATE, now, INTERVAL)
            data = data.rename(columns = {'value': metric})
            df = price.join(data, on='datetime', how='inner')

            price_values = df.price_usd.values
            data_values = df[metric].values

            correlation = pearsonr(price_values, data_values)
            new_row = {'metric': metric, 'correlation': correlation.statistic, 'pvalue': correlation.pvalue}
            print(new_row)
            correlation_df = correlation_df.append(new_row , ignore_index=True)
            
        except Exception as e:
            print(e)
            pass
        
    # save results
    correlation_df.to_csv(METRICS_CORRELATION_FILE)

if __name__ == '__main__':
    main()

