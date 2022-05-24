f=open('1.txt','a+')
print("Enter text @ for end:")
while(str!='@'):
    str=input("Enter text:")
    if(str!='@'):
        f.write(str+"\n")
 # put the file pointer in the biginning
f.seek(0,0)
a=f.read()
print(a)
f.close()
