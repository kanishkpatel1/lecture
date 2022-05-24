#print only 5 character of 1.txt file
f=open('1.txt','r')
a=f.read(5)
print(a)
f.close()