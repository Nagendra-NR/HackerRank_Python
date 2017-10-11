def average(array):
    # your code goes here
    set1 = set(array)
    return  sum(set1)/len(set1)
    
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
