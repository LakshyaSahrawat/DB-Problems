import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = company.merge(orders, how='inner', on='com_id', suffixes=('', '_right'))

    filter_df = merged_df[merged_df['name'] == 'RED']

    merge_filter_df = filter_df.merge(sales_person, how='inner', on='sales_id', suffixes=('','_right'))

    result = sales_person[~sales_person['name'].isin(merge_filter_df['name_right'])]
    result_df = result[['name']]

    return result_df