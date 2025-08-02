import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_counts = employee['managerId'].value_counts()
    
    managers_with_5_or_more = manager_counts[manager_counts >= 5].index
    
    result = employee[employee['id'].isin(managers_with_5_or_more)][['name']]
    
    return result