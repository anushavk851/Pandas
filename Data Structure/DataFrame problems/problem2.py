import pandas as pd
data = {
    "Employee": ["Arun", "Rahul", "Anu", "Meera", "Vishnu", "Diya"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
    "Salary": [35000, 28000, 42000, 30000, 32000, 45000],
    "Experience": [2, 1, 3, 2, 4, 5]
}

df = pd.DataFrame(data)
#1 Find the shape of the DataFrame.
print(df.shape)
#2 Find the average salary.
a=df['Salary']
print(a.sum()/a.count())
#3 Find the highest salary.
print(df['Salary'].max())
#4 Find the employee with the highest salary.
print(df[df['Salary']==df['Salary'].max()])
#5 Find employees whose salary is greater than 35000.
print(df[df['Salary']>35000])
#6 Find employees with experience greater than 2 years.
print(df[df['Experience']>2])
#7 Find employees working in the IT department.
print(df[df['Department']=="IT"])
#8 Find the total salary.
print(df['Salary'].sum())
#9 Find the average experience.
a=df['Experience']
print(a.mean())
#10 Sort employees by salary from highest to lowest.
print(df.sort_values(['Salary'][::-1]))
#11 Sort employees by experience from lowest to highest.
print(df.sort_values(['Experience']))
#12 Find the unique departments.
print(df['Department'].unique())
#13 Count how many employees belong to each department.
print(df['Department'].value_counts())
#14 Add a column called Annual_Salary:Salary × 12
df['Annual_Salary']=df['Salary']*12
print(df)
#15 Add a column called Senior:
    # Experience >= 3 → "Yes"
    # Experience < 3 → "No"
new=[]
for i in df['Experience']:
    if i>=3:
        new.append("Yes")
    else:
        new.append("No")
df['Senior']=new
print(df)
#16 Find the highest-paid employee and display only their name and salary.
a=df['Salary'].max()
emp=df[df['Salary']==a]
print(emp[['Employee','Salary']])
#17 Find all employees whose salary is above the average salary.
a=df['Salary']
b=a.mean()
print(df[df['Salary']>b])
#18 Find the employee with the maximum experience.
a=df['Experience'].max()
print(df[df['Experience']==a])
#19 Find the average salary of employees with experience >= 3.
a=df[df['Experience']>=3]
print(a['Salary'].mean())
#20 Sort the DataFrame by Department first and Salary second.
df.sort_values(['Department','Salary'])

