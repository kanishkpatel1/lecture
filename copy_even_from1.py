#copy even number of lines from one file to another file
f1=open('2.txt','r+')
f2=open('2a.txt','w')
r=f1.read()
a=f1.readlines()

for i in range(len(a)):
    if(i%2==1):
        f2.write(a[i])
f1.close()
f2.close()