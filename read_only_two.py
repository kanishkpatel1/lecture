#this program is for print only last two lines 
f=open('1.txt','r')
a=f.readlines()
b=len(a)
print(b) 

for i in a:
        print(a[b-2])
        print(a[b-1])