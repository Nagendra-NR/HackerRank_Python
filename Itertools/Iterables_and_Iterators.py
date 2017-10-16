from itertools import combinations

# first line is length of list
N = int(input()) # Not used anyway

#second line is the list of alphabets # a a c d
letters = input().split()

#third line is k
k = int(input())

comb_list = list(combinations(letters,k))
#[('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd'), ('c', 'd')]

a_list = [e for e in comb_list if 'a' in e]
#[('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd')]

print(len(a_list) / len(comb_list))
