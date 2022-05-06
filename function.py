
import numpy as np


maxx=1000

spot=0
for j in range(10):
    x=np.linspace(spot-maxx/10**j,spot+maxx/10**j,100)
    y=[]
    try:
        for k in range(len(x)):
            y.append(abs(2*x[k]+3-5))
    except:
        print("error")
    minn=10**200
    for i in range(len(y)):
        if y[i]<minn:
            minn=y[i]
            spot=x[i]







print(x[50])

