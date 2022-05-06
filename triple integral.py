from mathmod import *

def integrand(x,y,z):
    return x*y*z


def ib1(y): 
    return 0 #very inside bottom (ex. 2)

def it1(y):
    return 2 #very inside top (ex. 3*y)

def ib2(z):
    return 0 #middle bottom (ex. 2/z**3)

def it2(z):
    return z**2 #middle top (ex. sin(.5*z)


a,b=[0,4] #outside bottom, top
n=1000

cont1=1
summ=0

dd=2.2250738585072014e-308



go=(b-a)/n
w=a
count1=0

if (b-a)<.0001:
    cont1=0
while cont1==1:
    
    if count1%10==0:
        print(round(100*(w-a)/(b-a),5),"% done")
    count1+=1
    z=w
    d=it2(z)
    c=ib2(z)
    if count1==1:
        qi2=(d-c)/n+dd
    if count1!=1:
        qi2=(d-c)/n
    u=c
    cont2=1
    count2=0
    while cont2==1:
        y=u
        f=it1(y)
        e=ib1(y)
        if count2==0:
            qi1=(f-e)/n+dd
        if count2!=0:
            qi1=(f-e)/n
        count2+=1
        v=e
        cont3=1
        count3=0
        while cont3==1:
            x=v
            summ+=integrand(v,u,w)*qi1*qi2*go
            v+=qi1
            if v>f and qi1>0:
                cont3=0
            if v<f and qi1<0:
                cont3=0     
        u+=qi2
        if u>d and qi2>0:
            cont2=0
        if u<d and qi2<0:
            cont2=0
    w+=go
    if w>b and go>0:
        cont1=0
    if w<b and go<0:
        cont1=0
    

print(round(summ,3))
