import itertools
#Read S and k
S,k = list(input().split(' '))

#Get k length permutations od S in the list l
l = list(itertools.permutations(S,int(k)))

#sort l
l = sorted(l)

# join each permutation in the list and print 
for word in l :
    print ("".join(word))
