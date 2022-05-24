
from numpy import*
ar=[]
ca=[]

fi=[]
(r,c)=map(int,input("Enter the value of row and column:").split())
for i in range(r):
    a=list(map(int,input("Enter row values:").split()))
    ar.append(a)
x=array(ar)
print("matrix 1=",x)
for j in range(r):
    b=list(map(int,input("Enter row values:").split()))
    ca.append(b)
y=array(ca)
print("matrix2:",y)

for i in range(r):
    br=len(x[i])
    f=[]
    
    for j in range(br):
        sum=0
        for k in range(br):
            axa=x[i][k]*y[k][j]
            sum+=axa
        
        f.append(axa)
    fi.append(f)
final=array(fi)
print(final)
