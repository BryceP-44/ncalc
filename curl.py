x=2
y=2
z=2

i="y*z**2"
j="x*y"
k="y*z"



def Ry(k,x,y,z,h):
    ry=k.replace("x",str(x))
    ry=ry.replace("z",str(z))
    s1=ry.replace("y",str(y))
    s2=ry.replace("y",str(y+h))
    return (eval(s2)-eval(s1))/h
def Qz(j,x,y,z,h):
    qz=j.replace("x",str(x))
    qz=qz.replace("y",str(y))
    s1=qz.replace("z",str(z))
    s2=qz.replace("z",str(z+h))
    return (eval(s2)-eval(s1))/h
def Pz(i,x,y,z,h):
    pz=i.replace("x",str(x))
    pz=pz.replace("y",str(y))
    s1=pz.replace("z",str(z))
    s2=pz.replace("z",str(z+h))
    return (eval(s2)-eval(s1))/h
def Rx(k,x,y,z,h):
    rx=k.replace("y",str(y))
    rx=rx.replace("z",str(z))
    s1=rx.replace("x",str(x))
    s2=rx.replace("x",str(x+h))
    return (eval(s2)-eval(s1))/h
def Qx(j,x,y,z,h):
    qx=j.replace("y",str(y))
    qx=qx.replace("z",str(z))
    s1=qx.replace("x",str(x))
    s2=qx.replace("x",str(x+h))
    return (eval(s2)-eval(s1))/h
def Py(i,x,y,z,h):
    py=i.replace("x",str(x))
    py=py.replace("z",str(z))
    s1=py.replace("y",str(y))
    s2=py.replace("y",str(y+h))
    return (eval(s2)-eval(s1))/h
h=1/10000


a=Ry(k,x,y,z,h)-Qz(j,x,y,z,h)
b=Pz(i,x,y,z,h)-Rx(k,x,y,z,h)
c=Qx(j,x,y,z,h)-Py(i,x,y,z,h)

print(round(a,5),"i, ",round(b,5),"j, ",round(c,5),"k, ")
