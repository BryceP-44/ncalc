from math import *

def f(x,y):
    return 5


def ib(y):
    return 0

def it(y):
    return 1

n=2000
a,b=[0,1]

cont1=1
summ=0

dd=2.2250738585072014e-308
qo=(b-a)/n
u=a

#later=0
while cont1==1:
    y=u
    d=it(y)
    c=ib(y)
    qi=(d-c)/n+dd
    v=c
    cont2=1 
    while cont2==1:
        x=v
        summ+=f(v,u)*qi*qo
        v+=qi
        if v>d and qi>0:
            cont2=0
        if v<d and qi<0:
            cont2=0
            
    u+=qo
    if u>b and qo>0:
        cont1=0
    if u<b and qo<0:
        cont1=0

print(summ)
print(round(summ,2))


#take round of the real part of the answer
#charge of a plate and average value of a function
#centroid of lamina (also center of area)
#moment of intertia





