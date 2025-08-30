import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    prices['start_date'] = pd.to_datetime(prices['start_date'])
    prices['end_date'] = pd.to_datetime(prices['end_date'])
    units_sold['purchase_date'] = pd.to_datetime(units_sold['purchase_date'])

    df_merged = prices.merge(units_sold, how='left', on='product_id', suffixes=['_left', '_right'])

    mask = (df_merged['start_date'] <= df_merged['purchase_date']) & (df_merged['end_date'] >= df_merged['purchase_date'])

    df_merged = df_merged[mask | df_merged['purchase_date'].isna()]
    df_merged['units'] = df_merged['units'].fillna(0)

    df_merged['amount'] = df_merged['price'] * df_merged['units']
    
    res = df_merged.groupby('product_id').agg(
        total_amount=('amount', 'sum'),
        total_units=('units', 'sum')
    ).reset_index()

    res['average_price'] = res.apply(lambda row: round(row['total_amount'] / row['total_units'], 2) if row['total_units'] > 0 else 0, axis=1)
    res['average_price'] = res['average_price'].fillna(0)

    return res[['product_id', 'average_price']]
