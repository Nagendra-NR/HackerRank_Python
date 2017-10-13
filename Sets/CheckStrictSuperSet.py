# The first line contains the space separated elements of set 
A  = set(input().split())

#The second line contains integer n, the number of other sets. 
n = int(input())

check = True
for i in range(n):
    s = set(input().split())
    if (s.intersection(A) != s) or (s == A):
        check = False
        break
print(check)
