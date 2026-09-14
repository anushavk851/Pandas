import pandas as pd
one = pd.DataFrame({'id':[101,102,103,104],'Name':['Ammu','Sneha', 'Rasina','sajad'],
                    'subid':['sub1','sub2','sub3','sub4'],'Mark':[23,25,24,27]},index=[1,2,3,4])

two = pd.DataFrame({'id':[101,102,103,104],'Name':['Ammu1','Sneha1' ,'Rasina1','sajad1'],
                    'subid':['sub1','sub2','sub3','sub4'],'Mark':[24,28,29,19]},index=[1,2,3,4])

three = pd.DataFrame({'Name':['Ammu2','Sneha2','Rasina2', 'sajad2'],
                      'subid':['sub1','sub2','sub3','sub4'],
                      'Mark':[18,12,15,19],'rollno':[12,13,14,15]},index=[1,2,3,4])

#CONCATINATION ROW-WISE

print(pd.concat([one,two])) #concat one and two
pd.concat([three,two],keys=('x','y')) #to  mention different name to each dataset(three and two)
pd.concat([one,three],ignore_index=True) #to get continuation in output

#CONCATINATION COLUMN-WISE

print(pd.concat([one,two],axis=1))
pd.concat([three,two],keys=('x','y'),axis=1) #to  mention different name to each dataset(three and two)
pd.concat([one,three],ignore_index=True,axis=1) #to get continuation in output

#JOIN
#for joining dataset  based on certain rows similarity (eg id )we can use merge function
print(pd.merge(one,two,on=['id','subid']))
#type of join is mentioned using 'how'
print(pd.merge(one,two,on=['id','subid'],how='left')) #left join
