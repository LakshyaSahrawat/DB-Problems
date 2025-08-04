import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby('customer_number').count().reset_index().sort_values('order_number', ascending=False)[['customer_number']].head(1)