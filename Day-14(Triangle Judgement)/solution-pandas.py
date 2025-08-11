import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    def valid_triangle(row)->str:
        x = row['x']
        y = row['y']
        z = row['z']

        if x+y>z and y+z>x and z+x>y:
            return 'Yes'
        
        return 'No'

    triangle['triangle'] = triangle.apply(valid_triangle, axis=1)

    return triangle