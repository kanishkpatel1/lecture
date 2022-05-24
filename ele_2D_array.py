from numpy import*
a=[[1,2,3],[2,3,4],[4,5,6]]
for i in a:
    print(i)

#display element by element
for i in range (len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")

#method 2
print("\nmethod 2:")
for i in a:
    for j in i:
        print(j,end=" ")