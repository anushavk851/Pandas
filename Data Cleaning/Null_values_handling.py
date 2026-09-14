import pandas as pd
df=pd.read_csv(r'C:\Users\ACCURATE\Desktop\Data Science\EDA\Pandas EDA\sales dataset\sales_eda_dataset.csv')
df

#HANDLING NULL VALUES
#1 isnull()-check any missing value

print(df.isnull())  #return true or false to every element

print(df.isnull().sum()) # column wise null values

print(df.isnull().mean()*100)  #percentage 0f nullvalue of each column

print("Total null value count:",df.isnull().sum().sum()) #total null value count

print("City nullvalue count",df['City'].isnull().sum())  #displays the number of missing (NaN) values in the City column.

print(df[df['City'].isnull()]) #This displays all employees whose City value is missing (NaN).

print(df[df['Salesperson'].isnull()]) #This displays all employees whose Salesperson value is missing (NaN).
