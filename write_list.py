#Write a Python program to write a list to a file.
f=open('wr.txt','w')
lst=["kanishk","patel","royal"]
for i in lst:
    f.write(i+" ")
f.close() 