import pandas as pd
import numpy as np

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    first_logins = activity.groupby('player_id').agg({'event_date': 'min'}).reset_index()

    merged = first_logins.merge(activity, on='player_id', how='inner', suffixes=('_first', '_second'))
    second_logins = merged[merged['event_date_second'] - merged['event_date_first'] == pd.Timedelta(days=1)]
    fraction = np.round(len(second_logins)/len(first_logins), 2)
    result = pd.DataFrame({'fraction': [fraction]})

    return result