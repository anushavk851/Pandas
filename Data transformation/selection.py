import pandas as pd
data={
    "name":["Anu","Rahul","Karthik","Adarsh","Bindu"],
    "age":[24,25,30,28,20],
    "marks":[56,89,90,34,99],
    "location":["Kozhikode","Kannur","Thrissur","Palakkad","Kochi"]
}
df=pd.DataFrame(data)   #here key comes like column header.so all others are each series with common index value(keys)
print(df)

#selecting a column
print(df['name']) #o/p- is in format of series
#selecting multiple column
print(df[['name','location']]) #o/p in format of dataFrame

#selecting row-wise

#1 loc method-used for label based indexing
df=pd.DataFrame(data,index=["S1","S2","S3","S4","S5"])
print(df.loc['S1'])
print(df.loc['S1':'S4'])  #s4 also included(stop value)
print(df.loc['S1','name']) #s1th row and name -column

#2 iloc- integer location based indexing
print(df.iloc[0])
print(df.iloc[0:4]) #4 not included(stop value)
print(df.iloc[0,0]) #0th row and 0th column
