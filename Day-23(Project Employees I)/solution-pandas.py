import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = project.merge(employee, how='inner', on='employee_id')

    res = merged_df.groupby('project_id')['experience_years'].mean().reset_index()

    return res.rename(columns={'experience_years': 'average_years'}).round(2)