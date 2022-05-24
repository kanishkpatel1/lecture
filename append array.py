from array import*
x=array('i',[])  #empty array
n=int(input("Enter the number of elements that you want to store:"))
for i in range(n):
    
    x.append(int(input("Enter the elements:")))
print("Original array is",x)