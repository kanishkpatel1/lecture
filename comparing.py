from numpy import*
a=array([1,2,3,4,5])
b=array([2,1,3,4,5])
c=a==b
print(c)
c=a>b
print(c)
c=a<b
print(c)
print(any(c))  #return true if any elements is true 
print(all(c))   #return false if any element is false

#output-
# [False False  True  True  True]
# [False  True False False False]
# [ True False False False False]