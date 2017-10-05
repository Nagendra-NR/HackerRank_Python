def count_substring(string, sub_string):
    len_str = len(string)
    len_subStr = len(sub_string)
    
    count = 0
    
    for i in range(0,len_str) :
        tmpStr = string[i:i+len_subStr]
        if(tmpStr == sub_string):
            count = count + 1
      
    return count
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
