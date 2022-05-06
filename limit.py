import math

def floor(x):
    x=str(x)
    x=int(x[0])
    return(x)


def factorial(u):
    #fact=(2*3.14159*u)**.5 * (u/2.71828)**u
    for i in range(u):
        if i==1
    return fact

def sin(x,n):
    summ=0
    for i in range(n):
        pos= (-1)**i
        pi = 3.14159
        a= x*(pi/180)
        summ+= ((a**(2*i+1))/factorial(2*i+1))*pos
    return summ

x=360

n=10

print(round(sin(x,n),2))


a=[]
for i in range(100):
    a.append(sin(i,n))

print(a)

