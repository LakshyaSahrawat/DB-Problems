import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id',inplace=True)
    person.drop_duplicates(subset='email',keep='first', inplace=True)