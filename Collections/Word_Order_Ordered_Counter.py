from collections import Counter, OrderedDict

class OrderedCounter(Counter,OrderedDict):
    pass

# The above two lines helps to achieve method resolution order
# If we check output of help(counter) and help(OrderedCounter) in a python counter
"""
Counter
 |  Method resolution order:
 |      Counter
 |      __builtin__.dict
 |      __builtin__.object

OrderedCounter
 |  Method resolution order:
 |      OrderedCounter
 |      collections.Counter
 |      collections.OrderedDict
 |      __builtin__.dict
 |      __builtin__.object
"""

"""
What has changed is that now OrderedDict has been inserted in the order in which methods which be searched for when using OrderedCounter just before dict. So any of the dictionary methods will come OrderedDict instead of dict giving us the result we want.

This can be used on any class that inherits from dict and you want to keep the order of its key as that in which they are inserted. And in the more general case it can be used to create a new class uses and alternative implementation of some interface.

more info check : https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

"""
words = []
n = int(input())
for i in range(n):
    words.append(input().strip())
    
word_counter = OrderedCounter(words)

print(len(word_counter))

for word in word_counter:
    print(word_counter[word],end=' ')
