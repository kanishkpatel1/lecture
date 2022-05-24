f=open('1.txt','w')
a=input("Enter the string to input:")
f.write(a)
f.close()

f=open('1.txt','r')
a=f.read()
print(a)
f.close()