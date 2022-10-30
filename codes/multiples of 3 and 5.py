import numpy as np

arr = np.arange(1, 100)

print(arr[(arr%3 == 0) & (arr%5 == 0)])