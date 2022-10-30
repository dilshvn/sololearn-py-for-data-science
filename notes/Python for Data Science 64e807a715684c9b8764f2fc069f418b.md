# Python for Data Science

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

```jsx
import numpy as np

x = np.array([2, 1, 3])

x = np.append(x, 4)
x = np.delete(x, 0)
x = np.sort(x)

print(x) #[1 3 4]
```

np.delete() deletes the element of the given index and np.append() appends the given element

np.arange() creates an array that has a range of numbers similar to python range

```jsx
import numpy as np

x = np.arange(2, 10, 3)
print(x) #[2 5 8]
```