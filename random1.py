# import random   #without-->import numpy 
# a=random.random()
# print(a)
##output-->it will generate a random number between 0.0 to 1.0


# from numpy import*    #with numpy module
# a=random.rand()
# print(a)
##output-->it will generate a random number between 0.0 to 1.0



#que -->create a 1d array of 5 random elements with or without numpy
# from numpy import*     #with -->Numpy
# a=random.rand(5)
# print(a)
#output-->[0.5963976  0.73242651 0.93207306 0.67036892 0.22197802]

# import random   #without numpy 
# lst=[]                 #only use random module
# for i in range(5):
#     a=random.random()
#     lst.append(a)
# print(lst)

#output-->[0.626268632683692, 0.4165055211779498, 0.8707541468585873, 0.8143144811798997, 0.8880963789011845]

# #que--->Create a 2d array using rand()
# from numpy import*
# a=random.rand(2,2)
# print(a)

#random.rand.range(start,stop,step)
import random
a=random.randrange(0,9,1)  #this will return only one value from 0 to 8
print(a)
b=random.randint(0,9)    #this will return only one value from 0 to 9
print(b)