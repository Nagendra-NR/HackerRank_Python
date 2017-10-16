import itertools
#Read S and k
S,k = list(input().split(' '))

#range will break for k, so it should be k+1
for i in range(1,int(k)+1):
    l = list(itertools.combinations(sorted(S),i))
    for j in l:
       print(''.join(j))
