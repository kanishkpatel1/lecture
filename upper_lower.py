#count how many character are in upper case or in lower case
f=open('2.txt','r')
lower=0
upper=0
a=f.readlines()
for i in a:
    for j in i:
        if(j>='a' and j<='z'):
            lower+=1
        elif(j>='A' and j<='Z'):
            upper+=1
print("upper case characters are:",upper)
print("lower case characters are:",lower)
