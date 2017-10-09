def print_formatted(number):
    #number.strip()
    w = len(str(bin(number))[2:])
    for i in range(1,number+1,1):
        o = str(oct(i))[2:]
        h = str(hex(i))[2:]
        h = h.upper()
        b = str(bin(i))[2:]
        d = str(i)
        print('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(d,o,h,b,width=w))
