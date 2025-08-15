import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat = seat.sort_values('id').reset_index(drop=True)
    
    seat['new_id'] = seat['id']
    max_id = seat['id'].max()

    seat.loc[((seat['id'] % 2 == 1) & (seat['id'] + 1 <= max_id)), 'new_id'] = seat['id'] + 1
    seat.loc[(seat['id'] % 2 == 0), 'new_id'] = seat['id'] - 1
    
    merge_df = pd.merge(seat, seat[['id', 'student']], how='inner', left_on='new_id', right_on='id', suffixes=('', '_swapped'))
    
    swapped_df = merge_df[['new_id', 'student']].rename(columns={'new_id': 'id'})
    swapped_df = swapped_df.sort_values('id').reset_index(drop=True)

    return swapped_df