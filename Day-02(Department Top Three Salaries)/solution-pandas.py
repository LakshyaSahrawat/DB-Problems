import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby('departmentId')['salary'].rank(method='dense', ascending=False)

    merged_df = employee.merge(department, how='left', left_on='departmentId', right_on='id', suffixes=('', '_dept'))

    result_df = merged_df[merged_df['rank'] <= 3][['name_dept', 'name', 'salary']]

    result_df.columns = ['Department', 'Employee', 'Salary']

    return result_df