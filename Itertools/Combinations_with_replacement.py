import itertools
#Read S and k
S,k = list(input().split(' '))

l = list(itertools.combinations_with_replacement(sorted(S),int(k)))
for j in l:
    print(''.join(j))
