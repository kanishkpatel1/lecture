#bubble sort technique
from array import*
x=array('i',[])  #empty array
n=int(input("Enter the number of elements that you want to store:"))
for i in range(n):
        x.append(int(input("Enter the elements:")))
print("Original array is",x)
for i in range (n-1):
    for j in range (n-1-i):
        if(x[j]>x[j+1]):
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp
print("array in sorted is:",x)

