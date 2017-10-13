# First line contains no. of elements in set A
nA = int(input())

#second line contains the space separated list of elements in set .
A = set(list(map(int, input().split())))

#third line contains integer N, the number of other sets.
N = int(input())

for cmd in range(N) :
    #space separated entries of the operation name and the length of the other set.
    op, nB = input().split()  
   
    #space separated list of elements in the other set.
    #B = {int(x) for x in input().split()}
    B =  set(list(map(int, input().split())))
    
    if op=='update':
        A.update(B)
    elif op=='intersection_update':
        A.intersection_update(B)
    elif op=='difference_update':
        A.difference_update(B)
    elif op=='symmetric_difference_update':
        A.symmetric_difference_update(B)  
     
    
print(sum(A))
