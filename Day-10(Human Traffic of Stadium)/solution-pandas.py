import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    filter_df = stadium[stadium['people'] >= 100].copy()
    filter_df = filter_df.sort_values('id')
    filter_df['rank'] = range(1, len(filter_df) + 1)

    filter_df['grp'] = filter_df['id'] - filter_df['rank']

    join_df = filter_df.groupby('grp').size().reset_index(name='count')
    join_df = join_df[join_df['count'] >= 3]

    result_df = filter_df.merge(join_df, how='inner', on='grp', suffixes=['', '_right'])

    return result_df[['id', 'visit_date', 'people']]