import pandas as pd
data={
    "name":["Anu","Rahul","Karthik","Adarsh","Bindu"],
    "age":[24,25,30,28,20],
    "marks":[56,89,90,34,99],
    "location":["Kozhikode","Kannur","Thrissur","Palakkad","Kochi"]
}
df=pd.DataFrame(data)
df=pd.DataFrame(data,index=["S1","S2","S3","S4","S5"]) 
print(df) 

#1 marks greater than 90
print(df[df['marks']>90])
#2 marks>80 and age>20
print(df[(df['marks']>80) & (df['age']>20)])
#3 marks>90 or age>24
print(df[(df['marks']>90) | (df['age']>24)])
#4 marks not greater than 90
print(df[~(df['marks']>90)])
#5 To add new column
df['Grade']=["A","B","C","D","E"]
print(df)
#6 Creating new column from existing column eg: new column with (square of marks)
df['new_marks']= df['marks']*2
df['add_marks']= df['marks']+20
print(df)
#7 Modifying a column
df['marks']=df['marks']+2
print(df)
#8 Captitalize all letters in location
df['location']=df['location'].str.upper()
print(df)
#9 Dropping or deleting a column -It is used to delete rows or columns from a DataFrame.
df=df.drop("new_marks",axis=1)
print(df)

df.drop("add_marks", axis=1,inplace=True) #in pandas axis=1 is column and axis=0 is row
 #inplace=True --Make the change directly in the existing df.
print(df)
#10 Dropping a row using index(by default axis=0(rows))
df.drop("S2",inplace=True)
print(df)
#11 resetting Index
df=df.reset_index(drop=True)
#reset_index--It resets the row index of the DataFrame back to:0,1,2,3....
#drop=True--Reset the index, but don't keep the old index as a column.
print(df)
#12 adding rows using concat()
new={
    "name": "akhil",
    "age":20,
    "marks":95,
    "location":"Kozhikode",
    "Grade":"B"
}
new_df=pd.DataFrame(new,index=["S6"])
df=pd.concat([df,new_df])
print(df)    #here index is like 0,1,2,3,4,s6,s6 there is no continuation so we can use ignore_index=True to create continuation
#13 Index continuation while adding rows using concat() and ignore index
new={
    "name": "akhil",
    "age":20,
    "marks":95,
    "location":"Kozhikode",
    "Grade":"B"
}
new_df=pd.DataFrame(new,index=["S6"])
df=pd.concat([df,new_df],ignore_index=True)
print(df)
#14 unique value of specific column or categorical column
df['location'].unique()
#15 nunique-no of unique values
df['location'].nunique()
#16 value_count-value count of each unique element of a column
df['location'].value_counts()
#17  total mark
df['marks'].sum()



























