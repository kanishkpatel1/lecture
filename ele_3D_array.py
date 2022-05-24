from numpy import*
a=[[[1,2,3],
[4,5,6]],
[[7,8,9],
[10,11,12]]
]
print("3d array is ",a)
print("array by retrieving elements:") #we can also use len() method 
for i in a:
    for j in i:
        for k in j:
            print(k,end="\t")
        print()