
# Import Module
import math

def fac(x):
    for i in range(1,x+1):
        if i==1:
            fold=1
            f=1
        else:
            fold=f
            f=i*fold
    return f


# Create sine function
def sin( x, n):
    summ = 0
    for i in range(n):
        state = (-1)**i
        pi = 22/7
        a = x*(pi/180)
        summ += ((a**(2.0*i+1))/fac(2*i+1))*state
    return summ
 
# driver nodes
# Enter value in degree in x
x = 270
 
# Enter number of terms
n = 85
 
# call sine function
print(round(sin(x,n),2))
