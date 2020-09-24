import math

a=input()
a=int(a)

if a>=0:
    print(a)
elif a<0:
    print(-a)



#책에 나온 풀이

def abs_sign(a):
    if a>=0:
        return a
    else:
        return -a

def abs_square(a):
    b=a*a
    return math.sqrt(b)
