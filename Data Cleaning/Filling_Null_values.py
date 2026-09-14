import pandas as pd
df=pd.read_csv(r'C:\Users\ACCURATE\Desktop\Data Science\EDA\Pandas EDA\sales dataset\sales_eda_dataset.csv')
df
#FILLING NULL VALUES

#MODE
#we maily use mode to work with string data(non numerical like location,city)
#when ever we are using mode output will be series.but we want only in value not index so we give indexing to mode
mode_city=df['City'].mode()[0]
print(mode_city)

# #fillna()-usedfilling null values with a specified value
mode_city=df['City'].mode()[0]
df['City']=df['City'].fillna(mode_city)
print(df['City'])
print(df.isna().sum())

# #filling salesperson column
df['Salesperson']=df['Salesperson'].fillna(df['Salesperson'].mode()[0])
print(df.isna().sum()) #to check whether it is filled
#filling discount_percent column
df['Discount_Percent']=df['Discount_Percent'].fillna(df['Discount_Percent'].median() )
#here we use median instead of mean is because while using mean it will also may include outlier values which can cause error .
print(df.isna().sum())

#FFILL(-forward fill function
#if a value right in front of null value is not null then we can fill that null value with that value
df['City']=df['City'].ffill()
print(df.isnull().sum())

#BFILL()-backward fill
#if a value right in back of null value is not null then we can fill that null value with that value
df['Salesperson']=df['Salesperson'].bfill() 
print(df.isnull().sum())

#DROPNA()- delete rows or column
df.dropna()  #delete rows having null values(default axis =0)
#to remove column having null --remove complete column
df.dropna(axis=1)

#drop_duplicates()-to remove duplicate rows or exact same rows from dataset
df=df.drop_duplicates()
print(df.shape)

#Replace()-replacing a data with different data eg  M to male
df['Category']=df['Category'].replace({
    "Electronics":"El",
    "Accessories":"Ac"
})
print(df)

#Data Type conversion-
 #astype()-changes datatype of a column

#CHANGING DATATYPE OF ONE COLUMN
df['Discount_Percent']=df['Discount_Percent'].astype(int)   #converting a float to int
print(df)

#CHANGING DATATYPE OF MULTIPLE COLUMN
df[['Discount_Percent','Unit_Price']]=df[['Discount_Percent','Unit_Price']].astype(float)
print(df)

