import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    sales['rank'] = sales.groupby('product_id')['year'].transform(lambda x: x.rank(method='dense'))

    first_year = sales[sales['rank'] == 1]

    return first_year[['product_id', 'year', 'quantity', 'price']].rename(columns={"year": "first_year"})