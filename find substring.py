#find if substring is present or not
n=input("Enter the string to find:")
f=open('1.txt','r')
a=f.read()
if(n in a):
    print("present")
else:
    print("Not present")
f.close()