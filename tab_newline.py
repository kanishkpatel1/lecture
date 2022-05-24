#count how many spaces and tab and dot and new line in txt file
f=open('new.txt','r')
a=f.readlines()
print(len(a))
sp=0
d=0
ta=0
for i in a:
    for j in i:
        if(j==' '):
            sp+=1
        elif(j=="   "):#it works fine in ubuntu 
            ta+=1
        elif(j=="."):
            d+=1
print("space is :",sp)
print("lines are",len(a))
print("dots are: ",d)
print("tabs:",ta)