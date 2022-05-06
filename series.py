

def fac(x):
    for i in range(1,x+1):
        if i==1:
            fold=1
            f=1
        if i>1:
            fold=f
            f=i*fold
    return f

       



def sin(x,n):
    summ=0
    for i in range(n):
        state= (-1)**i
        pi=3.14159
        a = x*pi/180
        summ+=((a**(2*i+1))/fac(2*i+1))*state
    return round(summ,2)

print(sin(3600,85))



