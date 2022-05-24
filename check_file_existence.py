import os,sys

fname=input("Enter file name:")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname,"does not exist")

str=f.read()
print(str)
f.close()  #if the file not found it will give error