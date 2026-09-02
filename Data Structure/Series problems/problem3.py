marks = pd.Series([85, 72, 90, 65, 78],index=["Anu", "Asha", "Meera", "Riya", "Diya"])
#21 Display the marks of Meera.
print("marks of meera:",marks["Meera"])
#22 Display the marks of Anu and Riya.
print(marks["Anu"],"and",marks["Riya"])
#23 Find the student who scored the highest mark.
index_number=marks.argmax()
print("Topper:",marks.index[index_number])
#24 Find the student who scored the lowest mark.
lowest=marks.argmin()
print("Student who got the lowest:",marks.index[lowest])
#25 Calculate the average mark.
print("average mark:",marks.sum()/marks.count())
#or
print(marks.mean())
#26 Sort the Series according to the marks.
print("sorting in ascending:",marks.sort_values())
#27 Sort the Series according to the student names/index.
print("sorted by index:",marks.sort_index())
#28 Find how many students scored more than 75.
print("Number of students:", (marks > 75).sum())
 #here marks>75 is boolean value true.in list there are 3 value greater than 75 so it giive True as boolean which is represented as 1.
 # so its sum of 3 True(1) value is 3
#29 Find how many students scored less than 80.
print("students scored less than 80:",(marks<80).sum())
#30 Create a new Series containing only students who scored 80 or above.
new=marks[marks>79]
print(new)
