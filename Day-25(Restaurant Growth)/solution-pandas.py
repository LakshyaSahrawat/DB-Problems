import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    daily = (
        customer.groupby(customer["visited_on"].dt.normalize())["amount"]  # normalize = keep datetime at midnight
        .sum()
        .reset_index()
        .rename(columns={"visited_on": "day", "amount": "daily_amount"})
    )

    # 2. Calculate rolling 7-day sum (like window SUM in SQL)
    # Make sure data is sorted by day
    daily = daily.sort_values("day")
    daily["total_amount"] = daily["daily_amount"].rolling(window=7, min_periods=7).sum()

    # 3. Compute rolling average (divide by 7, like SQL round(.../7,2))
    daily["average_amount"] = (daily["total_amount"] / 7).round(2)

    # 4. Keep only rows where rolling window is full (like WHERE day >= min(day)+6)
    result = daily.dropna().reset_index(drop=True)

    return result[['day', 'total_amount', 'average_amount']].rename(columns = {'day': 'visited_on', 'total_amount': 'amount'})