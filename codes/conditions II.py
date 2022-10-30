import numpy as np

x = np.arange(1, 10)

print(x[(x>5) & (x%2==0)]) #[6 8]