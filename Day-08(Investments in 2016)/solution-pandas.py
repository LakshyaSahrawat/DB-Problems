import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['tiv_2015_count'] = insurance.groupby('tiv_2015')['tiv_2015'].transform('count')
    insurance['lon_lat_count'] = insurance.groupby(['lon', 'lat'])['pid'].transform('count')

    filter_df = insurance[(insurance['tiv_2015_count'] > 1) & (insurance['lon_lat_count'] == 1)]

    result = pd.DataFrame({'tiv_2016': [round(filter_df['tiv_2016'].sum(), 2)]})

    return result