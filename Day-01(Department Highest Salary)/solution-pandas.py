import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))

    merged_df['rank'] = merged_df.groupby('departmentId')['salary'].rank(method='dense', ascending=False)

    top_earners = merged_df[merged_df['rank'] == 1]

    result = top_earners[['name_dept', 'name', 'salary']]

    result.columns = ['Department', 'Employee', 'Salary']

    return result