import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    concat_df = pd.concat([
        request_accepted[['requester_id']].rename(columns={'requester_id': 'user_id'}),
        request_accepted[['accepter_id']].rename(columns={'accepter_id': 'user_id'})
    ])

    grouped_df = concat_df['user_id'].value_counts().reset_index()

    grouped_df.columns = ['user_id', 'frd_count']

    max_frd_count = grouped_df['frd_count'].max()

    result = grouped_df[grouped_df['frd_count'] == max_frd_count]
    result.columns = ['id', 'num']
    return result