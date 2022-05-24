from numpy import*
a=matrix('1 2 3; 4 5 6; 7 8 9')
print(a)
#getting diagonal elements
d=diagonal(a)
print("diagonal elements are",d)

# some operations on matrix
big=a.max()
small=a.min()
print("bigger element:",big)
print("Smaller element:",small)

print(a.sum())  #to print sum of all elements
print(a.mean()) # to print mean of all elements

#matrix sorting

b=matrix('10 2 32; 12 5 61; 17 22 19')
a=sort(b)  #this will sort row wise
print(a)
# output-[[ 2 10 32]
#          [ 5 12 61]
  #        [17 19 22]] 
a=sort(b,axis=0) #this will sort column wise
print(a)
# output-[[10  2 19]
#       [12  5 32]
#       [17 22 61]]

#transpose of a matrix
print("array before transpose:\n",b)

t=b.transpose()  #this will print transpose of the matrix
print("array after transpose:\n",t)
#2nd method to get transpose
t1=b.getT()
print("transpose using 2nd method:\n",t1)
