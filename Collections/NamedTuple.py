from collections import namedtuple
#The first line contains an integer N, the total number of students. 
N = int(input())

#The second line contains the names of the columns in any order. 
column_names = namedtuple('Student', input().split() )

#This will be a list of student tuples
Students_data = []

#The next N lines contains the marks, ID, name  and class, under their respective column names.
for i in range(N):
    data = input().split()
    Students_data.append(column_names(data[0], data[1], data[2], data[3]))

#Now the Students_data contain following data
# print (Students_data)
# Students_data = [Student(ID='1', MARKS='97', NAME='Raymond', CLASS='7'), Student(ID='2', MARKS='50', NAME='Steven', CLASS='4'), Student(ID='3', MARKS='91', NAME='Adrian', CLASS='9'), Student(ID='4', MARKS='72', NAME='Stewart', CLASS='5'), Student(ID='5', MARKS='80', NAME='Peter', CLASS='6')]

sum = 0

for student in Students_data :
    sum += float(student.MARKS)
    
print (sum/N)
