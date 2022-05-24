# enter 2 2d matrix by user input and find multiplication of matrix and transpose of 1 matrix 
# find maximum and minimum element 
# add and substract two matrix
# sample input   a=[1 2 3]      b=[10 11 12]
                #  [4,5,6]        [13 14 15]
                #  [7,8,9]        [16 17 18]

                # #1st output= [[ 1  2  3]
                #               [ 4  5  6]
                #               [ 7  8  9]
                #               [10 11 12]
                #               [13 14 15]
                #               [16 17 18]]

                # 2nd output= [1 2 3 10 11 12]
                #         [4 5 6 13 14 15]
                #         [7 8 9 16 17 18] 
from numpy import*
a=array([[1,2,3],
[4,5,6],
[7,8,9]])
print(a)

b=array([[10,11,12],
[13,14,15],
[16,17,18]])
print(b)

c=concatenate((a,b)) #for 1st output
print(c)

d=concatenate((a,b),axis=1)  #for 2nd output
print(d)
