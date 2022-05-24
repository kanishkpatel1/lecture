from numpy import*
a=array([0,200,0,41],int)
b=array([50,10,100,25] ,int)
c=where(a>b,a,b) # this will print those character that are bigger at particular index
print(c)
# to retrive indexes of non zero element from array a 
c=nonzero(a)
for i in c:
    print(a[c])