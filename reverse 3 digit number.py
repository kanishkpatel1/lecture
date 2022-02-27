number=int(input("enter the number"))
a=number//100
b=number%100    
c=b//10
d=b%10
print(d*100+c*10+a)

# 2nd method
n=int(input("enter the number"))
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
print("number in reverse is %d%d%d"%(a,b,c))