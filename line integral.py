from math import *

h=1/100000

#####
def xc(t):
    return 3-2*t
def yc(t):
    return 6-7*t
def zc(t):
    return 0
#####
    

def curve(t):
    x=xc(t)
    y=yc(t)
    z=zc(t)
    dx=(xc(t+h)-xc(t))/h
    dy=(yc(t+h)-yc(t))/h
    dz=(zc(t+h)-zc(t))/h
    return x,y,z,dx,dy,dz

def integrand(x,y,z):
    #####
    ing=3*x**2-2*y
    #####
    return ing

a=0
b=1
n=10000
q=(b-a)/n #chunk size
u=a
summ=0
z=0

for i in range(n):
    x,y,z,dx,dy,dz=curve(u)
    summ+=integrand(x,y,z)*(dx**2+dy**2+dz**2)**.5*q
    u+=q

print(round(summ,2))
