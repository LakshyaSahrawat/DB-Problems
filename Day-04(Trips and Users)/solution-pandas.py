import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    merge_df = trips.merge(users, left_on='client_id', right_on='users_id', suffixes=('', '_client'))
    merge_df = merge_df.rename(columns={'banned': 'banned_client'})
    merge_df = merge_df.merge(users, left_on='driver_id', right_on='users_id', suffixes=('', '_driver'))
    merge_df = merge_df.rename(columns={'banned': 'banned_driver'})
    merge_df['request_at'] = pd.to_datetime(merge_df['request_at'])

    filtered_df = merge_df[(merge_df['banned_client'] == 'No') & (merge_df['banned_driver'] == 'No') & (merge_df['request_at'].between('2013-10-01', '2013-10-03', inclusive='both'))]

    filtered_df['cancelled'] = filtered_df['status'].isin(['cancelled_by_driver', 'cancelled_by_client']).astype(int)

    result = (
        filtered_df.groupby('request_at')
        .agg(cancellation_rate=('cancelled', 'mean'))
        .reset_index()
    )

    result['cancellation_rate'] = result['cancellation_rate'].round(2)

    result = result.rename(columns={'request_at': 'Day', 'cancellation_rate': 'Cancellation Rate'})

    return result[['Day', 'Cancellation Rate']]