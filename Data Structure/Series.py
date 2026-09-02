# KEY FEATURES:

#1 Indexing:
    # Each element in a Series has a corresponding index, which can be used to access or manipulate the data.
    # print(series_from_list[0]) 
    # print(series_from_dict['b'])
    # O/P-1 2

#2 Vectorized Operations:
    # Series supports vectorized operations, allowing you to perform arithmetic operations on the entire series efficiently.
    # series_a = pd.Series([1, 2, 3])
    # series_b = pd.Series([4, 5, 6])
    # sum_series = series_a + series_b 
    # print(sum_series)
    #O/P-
    # 0    5
    # 1    7
    # 2    9
    # dtype: int64

#3 Alignment:
    # When performing operations between two Series objects, Pandas automatically aligns the data based on the index labels.
    # series_a = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    # series_b = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
    # sum_series = series_a + series_b 
    # print(sum_series)
    # Output:
    # a    NaN
    # b    6.0
    # c    8.0
    # d    NaN
    # dtype: float64

#4 NaN Handling:
    # Missing values, represented by NaN (Not a Number), can be handled gracefully in Series operations.
    # series_a = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    # series_b = pd.Series([4, 5], index=['b', 'c'])
    # sum_series = series_a + series_b 
    # print(sum_series)
    # Output:
    # a    NaN
    # b    6.0
    # c    8.0
    # dtype: float64





#Indexing 
test=pd.Series([10,20,30,40,50])
print(test) #we get index value along with the element in output
print(test[0]) #o/p-10 (indexing)

#Custom indexing
 #instead of getting default index we can set customized index for each elemnt
marks=pd.Series([10,20,30,40,50], index=["E","D","C","B","A"])
print(marks)
print(marks["A"]) #indexing

#SERIES FROM DICTIONARY
 #keys became index value
dict={
    "Anu":25,
    "rahul":50,
    "sree":36,
}
mark=pd.Series(dict)
print(mark)

#SERIES PROPERTY
dict={
    "Anu":25,
    "rahul":50,
    "sree":36,
}
mark=pd.Series(dict)

#INDEX ATTRIBUTES-to return index labels
print(mark.index)   #o/p-Index(['Anu', 'rahul', 'sree'], dtype='str')

#VALUES ATTRIBUTES-returns values
print(mark.values) #o/p-[25 50 36]

#DATATYPE-return datatype 
print(mark.dtype)   #o/p-int64

#DIMENSION
print(mark.ndim)    #o/p-1

#SHAPE
print(mark.shape)   #(3,)

#SIZE-return total number of elements
print(mark.size)  #o/p-3


#SERIES METHODS
test=pd.Series([10,20,30,40,50,60,70,80,90])
#1 Head(n)-to get first n values
print(test.head())  #by default return first 5 values
print(test.head(2))

#2 Tail(n)-to get last n values
print(test.tail()) #default 5 values
print(test.tail(3))

#3 Mean()
print(test.mean())

#4 Sum
print(test.sum())

#5 MIN() and MAX()
print(test.min())
print(test.max())

#6 Count()-returns non null count
print(test.count())
