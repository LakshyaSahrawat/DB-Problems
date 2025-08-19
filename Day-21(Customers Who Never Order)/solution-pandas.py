import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId', suffixes=('_left', '_right'))

    result_df = merge_df[merge_df['customerId'].isnull()][['name']].rename(columns=({"name": "Customers"}))

    return result_df