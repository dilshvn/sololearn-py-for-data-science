import pandas as pd

data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom', 'Harry'],
   'rank': [4, 1, 3, 5, 2, 6]
}

df = pd.DataFrame(data, index=data['name']) #index is optional here
user_rank = int(input())
print(df['name'][df['rank'] == user_rank])