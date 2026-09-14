import pandas as pd
data = {
    "Name": ["Anu", "Rahul", "Meera", "Arjun", "Diya", "Vishnu", "Asha"],
    "Age": [22, 25, 21, 24, 23, 26, 22],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales"],
    "Salary": [35000, 28000, 42000, 30000, 25000, 45000, 38000],
}
df=pd.DataFrame(data)
df

#unique--unique values of a chatagorical column
print(df['Department'].unique())

#nunique--Unique Value Count
print(df['Department'].nunique())

#Value_counts--Count of values in each department
print(df['Department'].value_counts())

#sum()
df['Salary'].sum()

#mean()-mean of salary
df['Salary'].mean()

#max()-maximum salary
df['Salary'].max()

#min()-minimum salary
df['Salary'].min()

#var()-variance
df['Salary'].var()
