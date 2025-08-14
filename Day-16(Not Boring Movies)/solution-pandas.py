import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    filter_cinema = cinema[~(cinema['description'].isin(['boring'])) & (cinema['id'] % 2 != 0)]

    return filter_cinema.sort_values(by='rating', ascending=False)