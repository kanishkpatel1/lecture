#wap to count the frequency of word
f=open('2.txt','r')
s=0
str=input("Enter the string to find its frequency:")
a=f.readlines()
c=[]
for i in a:
    b=i.split()
    for j in b:
        c.append(j)
for i in c:
    if(i==str): 
        s+=1
print(s)
f.close()
