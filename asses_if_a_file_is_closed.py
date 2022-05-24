f=open('1.txt','r')
print(f.closed) #here it will give false
f.close()
print(f.closed)  #here it will give true
