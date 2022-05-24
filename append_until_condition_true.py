#this program will append data while user input '@'
f=open('1.txt','a+')
while(str!='@'):
    str=input("Enter the string @ for end ")
    if(str!='@'):
        f.write(str)
f.seek(-5,2)
a=f.read()
print(a)