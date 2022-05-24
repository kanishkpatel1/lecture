import os,sys

fname=input("Enter file name:")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname,"does not exist")
cl=cw=cc=0
for i in f:
    word=i.split()
    cl+=1
    cw+=len(word)
    cc+=len(i)

  #print(i)
    #print(word)
print(cw,"are words",cl,"are lines",cc,"are characters")