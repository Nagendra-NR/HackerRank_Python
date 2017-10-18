from collections import OrderedDict
ordered_dictionary = OrderedDict()

number_of_items = int(input())

for i in range(number_of_items) :
    item, price = input().rsplit(' ',1)
    
    if item not in ordered_dictionary :
        ordered_dictionary[item] = int(price)
    else:
        ordered_dictionary[item] += int(price)
        
for item_name, net_price in ordered_dictionary.items():
    print (item_name, net_price)
