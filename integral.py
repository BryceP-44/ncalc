
def integrand(x):
    return 2*x**5

summ=0

a=0
b=2

n=100000
q=(b-a)/n
u=a

cont=1
while cont==1:
    summ+=integrand(u)*q
    u+=q
    if u>b and q>0:
        cont=0
    if u<b and q<0:
        cont=0

print(round(summ,5))
