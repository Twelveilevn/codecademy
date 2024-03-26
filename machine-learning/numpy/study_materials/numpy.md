ctrl + k + v
# NUMPY
- instead of python lists, we use numpy arrays

```python
import numpy as np

my_array = np.array([1,2,3,4])
my_list = [1,2,3,4]

my_array = np.array(my_list) #converts a list to an array

csv_array = np.genfromtxt('sample.csv', delimiter = ',')
```
## Basic array operations
```python
a = np.array([1,2,3,4,5])
a + 3 #adds 3 to each element ([4,5,6,7,8])
b = np.array([5,4,3,2,1])
a + b #([6,6,6,6,6])
```

## 1-D array selectors
```python
a = np.array([5,2,7,0,11])
a[0] #5
a[-1] #11
a[1:3] #([2,7]) [inclusive, exclusive]
a[:3] #([5,2,7])
a[-3:] #([7,0,11])
```

## 2-D array selectors
```python
a = np.array([[1,2,3,4],
            [10,20,30,40],
            [15,9,24,35]])

#a[row, column]
a[:,0] #selects the first column
a[1,:] #selects the second row
a[0,0:3] #selects first three elements of the first row
```

## Logical operations
```python
a > 5 #returns an array of booleans
a[a>5] #returns all elements that are greater than 5
a[(a>5) | (a<2)] #returns all elements within range
# | , &
```

## Statistics
- mean
```python
np.mean(array)
np.mean(array > 8) #0.2 (20% are greater than 8)
np.mean(2Darray) #mean of all axis
np.mean(2Darray, axis = 1) #mean of all rows
np.mean(2Darray, axis = 0) #mean of all columns
```
- outliers are identified by sorting the data with `np.sort(array)`
- median (middle value of the dataset or the mean of 2 central values)
    - `np.median(array)`
- percentiles
![percentiles image](../images/NumPy-40-percentile.webp)
    - `np.percentile(array, percentile)`
- standard deviation 
    - the larger the deviation the more spread out our data are from the center
    - `np.std(array)`