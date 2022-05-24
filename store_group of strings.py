
# to write a file untill user inpuT @ and write every string on new line
f=open('1.txt','w')
print("Enter text @ for end:")
while(str!='@'):
    str=input("Enter text:")
    if(str!='@'):
        f.write(str+"\n")  # here in (str+'/n') n is used for string in new line if we want in same line then--> (str+' ')

f.close()

#read all the strings of above code
f=open('1.txt','r')
a=f.read()
print(a)
f.close()
