import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product_sum = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    product_sum = product_sum[product_sum['product_key'] == len(product)]

    return product_sum[['customer_id']]