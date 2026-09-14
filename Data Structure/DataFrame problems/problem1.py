import pandas as pd
data = {
    "Name": ["Anu", "Asha", "Meera", "Riya", "Diya"],
    "Age": [22, 24, 21, 23, 25],
    "Mark": [85, 72, 90, 65, 78],
    "City": ["Kochi", "Calicut", "Kochi", "Kannur", "Calicut"]
}

df = pd.DataFrame(data)

#1 Display the entire DataFrame.
print(df)
#2 Find the number of rows and columns.
print("rows:",df.shape[0])
print("columns:",df.shape[1])
#3 Find the shape.
print(df.shape)
#4 Find the size.
print(df.size)
#5 Display the column names.
print(df.columns)
#6 Display the index.
print(df.index)
#7 Display the data types of all columns.
print(df.dtypes)
#8 Display information about the DataFrame using info().
print(df.info)
#9 Generate statistical information using describe().
print(df.describe)
#10 Display only the Name column.
print(df['Name'])
#11 Display only the Mark column.
print(df['Mark'])
#12 Display Name and Age.
print(df[['Name','Age']])
#13 Display the first 3 rows.
print(df.head(3))
#14 Display the last 2 rows.
print(df.tail(2))
#15 Display the row at index 2.
print(df.iloc[2])
#16 Display rows from index 1 to 3.
print(df.iloc[1:4])
#17 Display the Name and Mark of the student at index 3.
a=df.iloc[3]
print(a[['Name','Mark']])
#18 Display the students whose mark is greater than 75.
print(df[df['Mark']>75])
#19 Display the students whose age is greater than 22.
print(df[df['Age']>22])
#20 Display students from Kochi
print(df[df['City']=="Kochi"])
#21 Find the average age.
a=df['Age']
print(a.sum()/a.count())
#22 Find the average mark.
a=df['Mark']
print(a.sum()/a.count())
#23 Find the highest mark.
a=df['Mark']
print(a.max())
#24 Find the lowest mark.
a=df['Mark']
print(a.min())
#25 Find the total of all marks.
print(df['Mark'].sum())
#26 Find the median mark.
print(df['Mark'].median())
#27 Find the standard deviation of marks.
print(df['Mark'].std())
#28 Sort the DataFrame by Mark in ascending order.
print(df.sort_values(['Mark']))
#29 Sort the DataFrame by Mark in descending order.
print(df.sort_values(['Mark'])[::-1])
#30 Sort the DataFrame by Age.
print(df.sort_values(['Age']))
#31 Count the values in the City column.
a=df['City']
print(a.count())
#32 Find the unique cities.
a=df['City']
print(a.unique())
#33 Find the number of unique cities.
a=df['City']
unq=a.unique()
print(df['City'].nunique())
#or
print(len(unq))
#34 Check whether there are any missing values.
print(df.isnull().any().any())
#35 Display the first 2 rows using head().
print(df.head(2))
#36 Display the last 3 rows using tail().
print(df.tail())
#37 Add a new column called Gender:
    # Female
    # Female
    # Female
    # Female
    # Female

df['Gender']=['Female','Female','Female','Female','Female']
print(df)
#38 Add a new column called Pass where:
    # Mark ≥ 50 → "Pass"
    # Mark < 50 → "Fail"
new=[]
for i in df['Mark']:
    if i>=50:
        new.append("pass")
    else:
        new.append("Fail")
df['Pass']=new
print(df)
#39 Increase every student's mark by 5.
df['Mark']=df['Mark']+5
print(df)
#40 Create a new column Bonus_Mark containing the original mark + 5.
df['Bonus_Mark']=df['Mark']+5
print(df)
#41 Rename the column Mark to Marks.
df.rename(columns={'Mark': 'Marks'}, inplace=True)
print(df)
#42 Rename the column City to Location.
df.rename(columns={"City":"Location"},inplace=True)
print(df)
#43 Remove the Age column.
df.drop(columns="Age")
#44 Remove the row at index 2.
df.drop(index=2)
#45 Reset the index after removing a row.
df=df.drop(index=2)
df.reset_index()



















