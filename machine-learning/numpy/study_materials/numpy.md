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
- sum
```python
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for n in survey_responses if n == "Ceballos"])
print(total_ceballos)

>>> 33
```
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

### Statistical distributions
- Histograms
    - individual columns are called bins
    ```python
    from matplotlib import pyplot as plt
    data = np.array([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5])
    plt.hist(data, bins=1, range=(2,6)) #inclusive and exculsive
    plt.show()
    ```
    - classifing histograms based on the number of peaks
    ![unimodal](../images/unimodal_new.svg)
    ![bimodal](../images/bimodal_new.svg)
    ![multimodal](../images/multimodal_new.svg)
    ![uniform](../images/uniform_new.svg)
    - calssifing unimodal histogram by data distribution
    ![symmetric](../images/distribution-types-ii-symmetric-noline.svg)
    ![symmetric](../images/distribution-types-ii-symmetric.svg)
    ![skewright](../images/distribution-types-ii-skew-right-noline.svg)
    ![skewright](../images/distribution-types-ii-skew-right.svg)
    ![skewleft](../images/distribution-types-ii-skew-left-noline.svg)
    ![skewleft](../images/distribution-types-ii-skew-left.svg)
- Normal distribution
    - `np.random.normal(loc, scale, size)`
        - loc - mean for the normal distribution
        - scale - standard deviation of the distribution
        - size - number of random numbers to generate
- Data distribution
    - 68% of our samples will fall between +/- 1 standard deviation of the mean
    - 95% of our samples will fall between +/- 2 standard deviations of the mean
    - 99.7% of our samples will fall between +/- 3 standard deviations of the mean
- Binomial distribution
    - `np.random.binomial(N, P, size)`
        - N - number of samples
        - P - probability of success
        - size - number of experiments
        ```python
        # Let's generate 10,000 "experiments"
        # N = 10 shots
        # P = 0.30 (30% he'll get a free throw)

        a = np.random.binomial(10, 0.30, size=10000)

        plt.hist(a, range=(0, 10), bins=10, normed=True)
        plt.xlabel('Number of "Free Throws"')
        plt.ylabel('Frequency')
        plt.show()
        ```

        ```python
        #calculating the percantage chance of a player scooring 4 shots out of 10
        a = np.random.binomial(10, 0.30, size=10000)
        np.mean(a == 4)

        >>> 0.1973
        ```