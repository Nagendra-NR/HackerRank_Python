def swap_case(s):
    #Note : We cant modify s use a new string
    finalString = ""
    
    for c in s :
        if (c.islower()):
            finalString += c.upper()
        else :
            finalString += c.lower()
               
    return finalString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
