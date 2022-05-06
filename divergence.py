
x=1
y=1
z=1

i="y**2"
j="2*x*y+z**2"
k="2*y*z"

i=i.replace("y",str(y))
i=i.replace("z",str(z))

j=j.replace("x",str(x))
j=j.replace("z",str(z))

k=k.replace("x",str(x))
k=k.replace("y",str(y))

def f(t,i):
    i=i.replace("x",str(t))
    return eval(i)
def g(t,j):
    j=j.replace("y",str(t))
    return eval(j)
def r(t,k):
    k=k.replace("z",str(t))
    return eval(k)

h=1/1000000
a=round((f(x+h,i)-f(x,i))/h,5)
b=round((g(y+h,j)-g(y,j))/h,5)
c=round((r(z+h,k)-r(z,k))/h,5)

print(a+b+c)
