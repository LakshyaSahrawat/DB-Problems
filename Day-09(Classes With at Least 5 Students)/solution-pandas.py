import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    group_df = courses.groupby('class').size().reset_index(name='count')

    return group_df[group_df['count'] >= 5][['class']]