if __name__ == '__main__':
    List = []
    N = int(input())

    for i in range(N):
        tokens = input().split()
        if tokens[0] == 'insert':
            List.insert(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'print':
            print (List)
        elif tokens[0] == 'remove':
            List.remove(int(tokens[1]))
        elif tokens[0] == 'append':
            List.append(int(tokens[1]))
        elif tokens[0] == 'sort':
            List.sort()
        elif tokens[0] == 'pop':
             List.pop()
        elif tokens[0] == 'reverse':
            List.reverse()
