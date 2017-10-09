def capitalize(string):
    final_str = []
    for word in string.split(' ') :
        final_str.append(word.capitalize())
               
    return ' '.join(final_str)
    
if __name__ == '__main__':
string = input()
capitalized_string = capitalize(string)
print(capitalized_string)
