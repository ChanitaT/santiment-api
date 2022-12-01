from datetime import datetime, timezone, timedelta
import san

def utc_time(delta):
    delta_utc = datetime.now(timezone.utc) + timedelta(hours=delta)
    return delta_utc

def get_data(metric, slug, from_date, to_date, interval):
    try:
        data = san.get(
            metric,
            slug=slug,
            from_date=from_date,
            to_date= to_date,
            interval=interval,
            include_incomplete_data=True
        )
    except Exception as error:
            print(error)
    return data


    