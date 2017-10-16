from itertools import groupby
S = list(map(int, input()))
final_list = []

for i,j in groupby(S) :
    l = list(j)    
    final_list.append( [len(l), i]) 
        
for item in final_list :
    print (  "(" + str(item[0]) +", " + str(item[1]) + ")", end=' ') 
