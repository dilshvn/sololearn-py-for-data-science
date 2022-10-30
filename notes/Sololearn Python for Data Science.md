# Sololearn: Python for Data Science

## Statistics

## Measures of Central Tendancy

Mean is the average value of the dataset. Median is the middle value of an ordered dataset.

Median is more useful than mean because mean can vary widely due to one value that is lot larger/smaller than others.

## Standard Deviation

Standard deviation is a measure of how spread the data is. Standard deviation  is the square root of variance. 

If standard deviation is 17.1 and mean is 33.1, values that are within one standard deviation is said to be between (33.1-17.1) and (33.1+17.1)

Low standard deviation means values tend to be close to the mean and vise versa

## NumPy (Numerical Python)

To use NumPy, first import the library

```jsx
import numpy as np
```

## NumPy Arrays

NumPy arrays are faster and more compact than lists. They are homogeneous, meaning only single data type elements can be stored. NumPy array can be created as follows

```jsx
x = np.array([1, 2, 3, 4])
```

Their elements can be accessed using indexes

```jsx
print(x[0])
```

NumPy arrays are called ndarrays, meaning ‘N-dimensional arrays’, because they can have multiple dimensions

```jsx
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x[1][2])
```

This is a 2d array which has 3 rows and 3 columns

## NumPy Array Properties

```jsx
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(x.ndim) # 2
print(x.size) # 9
print(x.shape) # (3, 3)
```

ndim returns number of dimensions of array. size returns total number of elements of array. 

shape returns a tuple of integers that indicate the number of elements stored in each dimension of the array. Here, (3, 3) means 3 rows and 3 columns in this 2d array.

We can add, remove and sort using np.append(), np.delete(), and np.sort()

```python
import numpy as np

x = np.array([2, 1, 3])

x = np.append(x, 4)
x = np.delete(x, 0)
x = np.sort(x)

print(x) #[1 3 4]
```

np.delete() deletes the element of the given index and np.append() appends the given element

np.arange() creates an array that has a range of numbers similar to python range

```python
import numpy as np

x = np.arange(2, 10, 3)
print(x) #[2 5 8]
```

## Reshape

```python
import numpy as np

x = np.arange(1, 7)

z = x.reshape(3, 2)

print(z) 

'''
[[1 2]
 [3 4]
 [5 6]]
'''
```

Here, 1d array containing 6 elements is reshaped to 2d array with 3 rows and 2 columns. Number of elements should be same at reshaping. 

Reshape can also do the opposite

```python
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])

z = x.reshape(6)

print(z) #[1 2 3 4 5 6]
```

Here, 2d array is reshaped to a 1d array. This flat array can also be achieved using flatten() function

## Indexing and Slicing

Can be indexed and sliced similar to Python lists

```python
import numpy as np

x = np.arange(1, 10)

print(x[0:2])
print(x[5:])
print(x[:2])
print(x[-3:])
```

## Conditions

Here, elements that are less than 4 are selected

```python
import numpy as np

x = np.arange(1, 10)

print(x[x<4]) #[1 2 3]
```

& and | can be used with conditions

```python
import numpy as np

x = np.arange(1, 10)

print(x[(x>5) & (x%2==0)]) #[6 8]
```

## Operations

sum() is used to find sum of all elements

```python
import numpy as np

x = np.arange(1, 10)
print(x.sum()) #45
```

min(), max() is used to find smallest and largest elements

## Broadcasting

Performing given operation with each element is called broadcasting

```python
import numpy as np

x = np.arange(1, 10)
y = x*2

print(y) #[ 2  4  6  8 10 12 14 16 18]
```

## Statistics with NumPy

NumPy has direct dunctions for statistics

```python
import numpy as np

x = np.array([14, 18, 19, 24, 26, 33, 42, 55, 67])

print(np.mean(x))
print(np.median(x))
print(np.var(x))
print(np.std(x))
```

## Pandas (Panel Data)

Pandas is used to read, extract data from files and transform, analyze, calculate statistics, etc

First, import pandas to use

```python
import pandas as pd
```

## Series and DataFrames

A series is a column while dataframe is a multi-dimensional table consisting of a collection of series

Series is  a 1d array and dataframe is a multi-dimensional array

## Creating a DataFrame

Let’s use a dictionary to create a dataframe

```python
import pandas as pd

data = {
   'ages': [14, 18, 24, 42],
   'heights': [165, 180, 176, 184]
}

df = pd.DataFrame(data)
print(df) #crates a table with data
```

This dataframe has 2 columns. Dataframe automatically creates a numeric index for each row. We can specify a custom index.

```python
import pandas as pd

data = {
   'ages': [14, 18, 24, 42],
   'heights': [165, 180, 176, 184]
}

df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
print(df)
```

We can access a row using its index and loc[] function

```python
import pandas as pd

data = {
   'ages': [14, 18, 24, 42],
   'heights': [165, 180, 176, 184]
}

df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
print(df.loc["Bob"])
```

This will show data related to Bob such as age and height.