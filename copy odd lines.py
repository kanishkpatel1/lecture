#copy odd number of lines from one file to another file
f1=open('al.txt','r+')
f2=open('2.txt','w')
a=f1.readlines()
for i in range(len(a)):
    if(i%2==0):
        f2.write(a[i])

f1.close()
f2.close()