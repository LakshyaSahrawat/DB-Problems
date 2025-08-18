import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    group_df = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    filter_df = group_df[group_df['timestamp'] >= 3]
    return filter_df[['actor_id', 'director_id']]