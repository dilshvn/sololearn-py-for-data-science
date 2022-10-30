import pandas as pd

data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
   'number': ['1234', '5678', '2222', '1111', '0909']
}

df = pd.DataFrame(data, index = ['James', 'Billy', 'Bob', 'Amy', 'Tom'])

print(df.loc[input()])