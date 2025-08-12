import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers['cnt'] = my_numbers.groupby('num')['num'].transform('count')

    unique_numbers = my_numbers[my_numbers['cnt'] == 1]

    if unique_numbers.empty:
        return pd.DataFrame({'num': [None]})

    max_unique_num = unique_numbers['num'].max()

    return pd.DataFrame({'num': [max_unique_num]})