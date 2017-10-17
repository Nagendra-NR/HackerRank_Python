from collections import Counter
earning = 0
#First line = X = number of shoes
X = int(input())

#Second line = list of all shoe size in shop
shoe_size_list = list(map(int, input().split()))
shoe_size_count = dict(Counter(shoe_size_list))
#print (shoe_size_count)

#third line = N = number of customers
N =  int(input())

#next N lines = shoesize, prize
for i in range(N):
    size, price = map(int, input().split())
    if size in shoe_size_count and shoe_size_count[size] > 0:
        #print(str(size) + " is pesent with price" + str(price) )
        earning += price
        shoe_size_count[size] -= 1

print(earning)   
