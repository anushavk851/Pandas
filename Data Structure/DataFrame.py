#KEY FEATURES:
#1 Indexing:
    # provides flexible indexing options,allowing access to rows,columns,or individual elements based on labels or integer positions.
    # data = {'Name': ['John', 'Alice', 'Bob'],
    #         'Age': [25, 30, 35],
    #         'City': ['New York', 'Los Angeles', 'Chicago']}
    # Accessing a column
    # print(df['Name'])
    # # Accessing a row by label
    # print(df.loc[0])
    # Accessing a row by integer position
    # print(df.iloc[0])
    # Accessing an individual element
    # print(df.at[0, 'Name'])

#2 Column Operations:
    # Columns in a DataFrame are Series objects, enabling various operations such as arithmetic operations, filtering, and sorting.

    # Adding a new column
    # df['Salary'] = [50000, 60000, 70000]
    # Filtering rows based on a condition
    # high_salary_employees = df[df['Salary'] &gt; 60000]
    # print(high_salary_employees)
    # Sorting DataFrame by a column
    # sorted_df = df.sort_values(by='Age', ascending=False)
    # print(sorted_df)

    # Output:
    #   Name  Age     City  Salary
    # 2  Bob   35  Chicago   70000

    #     Name  Age         City  Salary
    # 2    Bob   35      Chicago   70000
    # 1  Alice   30  Los Angeles   60000
    # 0   John   25     New York   50000

#3 Missing Data Handling:
    # DataFrames provide methods for handling missing or NaN values, including dropping or filling missing values.
    # Dropping rows with missing values
    # df.dropna()
    # print(df)
    # Filling missing values with a specified value
    # df.fillna(0)
    # print(df)

    # Output:
    #     Name  Age         City  Salary
    # 0   John   25     New York   50000
    # 1  Alice   30  Los Angeles   60000
    # 2    Bob   35      Chicago   70000

    #     Name  Age         City  Salary
    # 0   John   25     New York   50000
    # 1  Alice   30  Los Angeles   60000
    # 2    Bob   35      Chicago   70000

#4 Grouping and Aggregation:
    # DataFrames support group-by operations for summarizing data and applying aggregation functions.
    # Grouping by a column and calculating mean
    # avg_age_by_city = df.groupby('City')['Age'].mean()
    # print(avg_age_by_city)
    # Output:
    # City
    # Chicago        35.0
    # Los Angeles    30.0
    # New York       25.0
    # Name: Age, dtype: float64

data={
    "name":["Anu","Rahul","Karthik","Adarsh","Bindu"],
    "age":[24,25,30,28,20],
    "marks":[56,89,90,34,99],
    "location":["Kozhikode","Kannur","Thrissur","Palakkad","Kochi"]
}
df=pd.DataFrame(data)   #here key comes like column header.so all others are each series with common index value(keys)
print(df)
print(df['name'])
df=pd.DataFrame(data,index=["S1","S2","S3","S4","S5"]) #costomization of index

data={
    "name":["Anu","Rahul","Karthik","Adarsh","Bindu"],
    "age":[24,25,30,28,20],
    "marks":[56,89,90,34,99],
    "location":["Kozhikode","Kannur","Thrissur","Palakkad","Kochi"]
}
#PROPERTIES
#1 Shape
print(df.shape)
#2 Size
print(df.size)
#3 dimension
print(df.ndim)
#4 column header-returns col names or keys
print(df.columns)
#5 index- returns row labels
print(df.index)
#6 dtypes-to check datatype of a dataFrame
print(df.dtypes)


#METHODS
data={
    "name":["Anu","Rahul","Karthik","Adarsh","Bindu"],
    "age":[24,25,30,28,20],
    "marks":[56,89,90,34,99],
    "location":["Kozhikode","Kannur","Thrissur","Palakkad","Kochi"]
}
#1 Head()-return first n rows
print(df.head()) #default first 5 rows
print(df.head(2)) #first 2 rows

#2 Tail-returns last n rows
print(df.tail()) #default last 5 rows
print(df.tail(3)) #last 3 rows

#3 INFO()-returns complete information of a dataframe(gives corresponding class,number of entryes,number of colum),non null count,total rows,memory usage etc..
print(df.info())

#4 describe()-to get statiistical summary of numerical col(like mean,median,mode,varience....)
print(df.describe())
print(df.describe(include="all"))
