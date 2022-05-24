#Write a python program to find the longest words.
f=open('al.txt','r')
a=f.readlines()
c=[]
lst=[]
for i in a:
    b=i.split()
    for j in b:
        c.append(j)
for i in range(len(c)-1):
    if(len(c[i+1])>len(c[i])):
        l=c[i+1]
    else:
        l=c[i]
print(l)
f.close()
#print("longest word is",b[d-1])