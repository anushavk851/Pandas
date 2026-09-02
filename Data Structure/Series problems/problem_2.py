import pandas as pd
s = pd.Series([25, 40, 15, 60, 35, 80, 50])
# Find the sum of all values.
print("sum:",s.sum())
#8 Find the mean.
print("mean:",s.mean())
#9 Find the median.
print("median:",s.median())
#10 Find the maximum value.
print("Maximum value:",s.max())
#11 Find the minimum value.
print("minimum value:",s.min())
#12 Find the standard deviation.
print("Standard Deviation:",s.std())
#13 Find the variance.
print("Variance:",s.var())
#14 Sort the Series in ascending order.
print("sorting in ascending:",s.sort_values())
#15 Sort the Series in descending order.
print("sorting in descending:",s.sort_values()[::-1])
#16 Display the first 3 values.
print("first 3 values:",s.head(3))
#17 Display the last 3 values.
print("last 3 values:",s.tail(3))
#18 Count the number of values.
print("number of values:",s.count())
#19 Find the value at index 3.
print("value at index 3:",s[3])
#20 Find the index of the maximum value.
print("index of maximum:",s.argmax())
