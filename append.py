#append in .txt file 
str=input("Enter the string to append:")
a=int(input("Enter the position:"))
f=open('1.txt','r+')
f.seek(a,0)
a=f.write(str)
f.close()

f=open('1.txt','r')
a=f.read()
print(a)
f.close()



