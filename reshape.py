import numpy as np  #in arange function (from numpy import*) not work
a=np.arange(10)  #this will arange values from 0 to 9

print(a)
print("using reshape (2,5\n)")
b=a.reshape(2,5) #change the shape as 2 rows and 5 columns
print(b)
print("using reshape(5,2\n")
c=a.reshape(5,2) #change the shape as 5 rows and 2 columns
print(c)

#flatten method() will convert array into 1d
print("after using flatten method():")
d=c.flatten()
print(d)
0
arr=np.arange(20)
e=arr.reshape(2,2,5) #two array each with two rows and 5 columns
print(e)