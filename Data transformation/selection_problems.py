import pandas as pd
data = {
    "Name": ["Anu", "Rahul", "Meera", "Arjun", "Diya", "Vishnu", "Asha"],
    "Age": [22, 25, 21, 24, 23, 26, 22],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales"],
    "Salary": [35000, 28000, 42000, 30000, 32000, 45000, 38000],
    "City": ["Kochi", "Calicut", "Kochi", "Kannur", "Calicut", "Kochi", "Kollam"]
}

df = pd.DataFrame(data)

#1 Display only the Name column.
print(df['Name'])
#2 Display only the Salary column.
print(df['Salary'])
#3 Display the Name and Age columns.
print(df[['Name','Age']])
#4 Display the Name, Department, and Salary columns.
print(df[['Name','Department','Salary']])
#5 Display the Age, Salary, and City columns.
print(df[['Age','Salary','City']])
#6 Display all columns except City.
print(df[['Name','Age','Department','Salary']])
#7 Display all columns except Age and Salary.
print(df[['Name','Department','City']])
#8 Store the Name column in a new variable called names.
a=df['Name']
print(a)
#9 Store the Name and Salary columns in a new DataFrame called employee_salary.
employee_salary=df[['Name','Salary']]
print(employee_salary)
#10 Display the Department column and check its type.
a=df['Department']
print(a)
print(a.dtypes)
#11 Display the first row.
print(df.loc[0])
#12 Display the third row.
print(df.loc[2])
#13 Display the last row.
print(df.iloc[-1])
#14 Display the first 3 rows.
print(df.head(3))
#or
print(df.iloc[0:3])
#15 Display rows from index 2 to index 5.
print(df.iloc[2:6])
#16 Display the first 4 rows and only the first 2 columns.
a=df.iloc[0:4]
print(a[['Name','Age']])
#17 Display rows 1, 3, and 5.
print(df.iloc[1:6:2])
#18 Display the last 3 rows.
print(df.iloc[-3:])
#19 Display the second row and only the Name and Salary columns.
a=df.iloc[1]
print(a[['Name','Salary']])
#20 Display rows 2–5 and columns Name, Department, and Salary.
a=df.iloc[2:6]
print(a[['Name','Department','Salary']])
#21 Set the employee names as the DataFrame index: df = df.set_index("Name"),Then display the row belonging to Meera.
df=df.set_index("Name")
print(df.loc['Meera'])
#22 Display the row belonging to Anu.
#df=df.set_index("Name")
print(df.loc['Anu'])
#23 Display the rows belonging to Anu and Diya.
#df=df.set_index("Name")
print(df.loc[['Anu','Diya']])
#24 Display the Salary of Vishnu.
#df=df.set_index("Name")
a=df.loc['Vishnu']
print(a['Salary'])
#25 Display the Department and City of Rahul.
#df=df.set_index("Name")
a=df.loc['Rahul']
print(a[['Department','City']])
#26 Display the Age and Salary of Meera.
#df=df.set_index("Name")
a=df.loc['Meera']
print(a[['Age','Salary']])
#27 Display all information about Arjun and Asha.
#df=df.set_index("Name")
print(df.loc["Arjun"])
print()
print(df.loc["Asha"])





