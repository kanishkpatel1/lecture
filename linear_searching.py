from array import*
x=array('i',[])  #empty array
n=int(input("Enter the number of elements that you want to store:"))
for i in range(n):
        x.append(int(input("Enter the elements:")))
print("Original array is",x)
el=int(input("Enter the element to search:"))
# for i in range (n):
#     if(x[i]==el):
#         print("Element found at position ",i+1)
#     else:
#         print("Element not found:")  #this is method 1

#for i in x:
#    if(i==el):
#        print("Element found at position",i)  #this is another method

#using indexing method
try:
    pos=x.index(el)
    print("Element found at position",pos+1)
except ValueError:
    print("Element not found:")
