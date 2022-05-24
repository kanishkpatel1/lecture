#Write a python program to remove new line character
f=open('n.txt','r+')
flist=f.readlines()
[print(l.strip()) for l in flist]

