import pandas as pd

def return_type(df):
    if pd.isna(df['p_id_left']):
        return 'Root'
    elif pd.notna(df['id_right']) and pd.notna(df['p_id_left']):
        return 'Inner'
    else:
        return 'Leaf'

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    merged_tree = tree.merge(tree, how='left', left_on='id', right_on='p_id', suffixes=('_left', '_right'))

    merged_tree['type'] = merged_tree.apply(return_type, axis=1)
    merged_tree.drop_duplicates(subset='id_left', inplace=True)
    merged_tree.sort_values(by='id_left', inplace=True)

    return merged_tree[['id_left', 'type']].rename(columns={'id_left': 'id'})