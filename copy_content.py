#Write a Python program to copy the contents of a file to another file

f1=open('cp.txt','r+')
f2=open('cp1.txt','w')
a=f1.readlines()
for i in range(len(a)):

        f2.write(a[i])

f1.close()
f2.close()