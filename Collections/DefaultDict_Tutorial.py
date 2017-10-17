from collections import defaultdict

defaultd = defaultdict(list)

#The first line contains integers, n and m separated by a space. 
n, m = map(int, input().split())

#The next  lines contains the words belonging to group A. 
for i in range(n):
    aword = input()
    defaultd[aword].append(str(i+1))\

# dictionary key is the words in group A, 
# Value is the list of  indices where they appear
# print (defaultd)  #{'b': ['3', '5'], 'a': ['1', '2', '4']}
    
#The next  lines contains the words belonging to group B.    
for j in range(m) :
    bword = input()
    print(' '.join(defaultd[bword]) or -1)
