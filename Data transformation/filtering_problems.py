import pandas as pd
data = {
    "Name": ["Anu", "Rahul", "Meera", "Arjun", "Diya", "Vishnu", "Asha"],
    "Age": [22, 25, 21, 24, 23, 26, 22],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales"],
    "Salary": [35000, 28000, 42000, 30000, 32000, 45000, 38000],
    "City": ["Kochi", "Calicut", "Kochi", "Kannur", "Calicut", "Kochi", "Kollam"]
}

df = pd.DataFrame(data)

#1 Display employees whose age is greater than 23.
print(df[df['Age']>23])

#2 Display employees whose age is less than 24.
print(df[df['Age']>24])

#3 Display employees whose salary is greater than 35000.
print(df[df['Salary']>35000])

#4 Display employees whose salary is less than 35000.
print(df[df['Salary']<35000])

#5 Display employees whose salary is exactly 30000.
print(df[df['Salary']==30000])

#6 Display employees who work in the IT department.
print(df[df['Department']=='IT'])

#7 Display employees who live in Kochi.
print(df[df['City']=="Kochi"])

#8 Display employees who live in Calicut.
print(df[df['City']=="Calicut"])

#9 Display employees whose age is equal to 22.
print(df[df['Age']==22])

#10 Find employees whose age is greater than 22 AND salary is greater than 35000.
print(df[(df['Age']>22)& (df['Salary']>35000)])

#11 Find employees whose age is less than 24 AND department is IT.
print(df[(df['Age']<24)&(df['Department']=="IT")])

#12 Find employees whose salary is greater than 30000 AND city is Kochi.
print(df[(df['Salary']>30000)&(df['City']=="Kochi")])

#13 Find employees who work in IT AND have salary above 40000.
print(df[(df['Department']=="IT") & (df['Salary']>40000)])

#14 Find employees who work in HR OR Sales.
print(df[(df['Department']=="HR") |(df['Department']=="Sales")])

#15 Find employees who live in Kochi OR Calicut.
print(df[(df['City']=="Kochi") | (df['City']=="Calicut")])

#16 Find employees whose salary is between 30000 and 40000.
print(df[(df['Salary']<40000) & (df['Salary']>30000)])

#17 Find employees whose age is between 22 and 25.
print(df[(df['Age']>22) & (df['Age']<25)])

#18 Find employees whose salary is greater than 35000 AND age is greater than 23.
print(df[(df['Salary']>35000) & (df['Age']>23)])

#19 Display only the Name and Salary of employees whose salary is greater than 35000.
a=df[df['Salary']>35000]
print(a[['Name','Salary']])

#20 Display only Name and Department of employees working in IT.
a=df[df['Department']=="IT"]
print(a[['Name','Department']])

#21 Display only Name and City of employees from Kochi.
a=df[df['City']=="Kochi"]
print(a[['Name','City']])

#22 Display only Name, Age, and Salary of employees older than 23.
a=df[df['Age']>23]
print(a[['Name','Age','Salary']])

#23 Display only Name and Salary of employees whose salary is between 30000 and 40000.
a=df[(df['Salary']>30000) &(df['Salary']<40000)]
print(a[['Name','Salary']])

#24 Display Name, Department, and Salary of employees working in IT with salary above 40000.
a=df[(df['Department']=="IT") &(df['Salary']>40000)]
print(a[['Name','Department','Salary']])

#25 Display Name and Age of employees who live in Calicut.
a=df[df['City']=="Calicut"]
print(a[['Name','Age']])

#26 Find the Name and Salary of employees earning more than 35000.
a=df[df['Salary']>35000]
print(a[['Name','Salary']])

#27 Find the Name and Department of employees whose age is less than 24 and salary is greater than 30000.
a=df[(df['Age']<24) & (df['Salary']>30000)]
print(a[['Name','Department']])

#28 Find all details of employees who are from Kochi and work in IT.
a=df[(df['Department']=="IT") & (df['City']=="Kochi")]
print(a)

#29 Find the Name, City, and Salary of employees whose salary is above 32000.
a=df[df['Salary']>32000]
print(a[['Name','City','Salary']])

#30 Find all employees who are not from Kochi.
a=df[~(df['City']=="Kochi")]
print(a)

#31 Find all employees who are not working in IT.
print(df[~(df['Department']=="IT")])

#32 Find all employees whose salary is not equal to 30000.
print(df[~(df['Salary']==30000)])

#33 Find the Name and Salary of employees whose age is greater than 22 and who are not from Kochi.
a=df[(df['Age']>22) & ~(df['City']=="Kochi")]
print(a[['Name','Salary']])





