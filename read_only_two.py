#this program is for print only last two lines from last
f=open('al.txt','r')
a=f.readlines()
print(a)
b=len(a)
print(b) 

for i in a:
        print(a[b-2])
        print(a[b-1])