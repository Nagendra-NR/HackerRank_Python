#from cmath import phase
#z = complex(input())
#print(abs(z))
#print(phase(z))

import cmath
z = complex(input())
p = cmath.polar(z)
print(p[0])
print(p[1])
