n=int(input("Enter the number of unit : "))
if(n<=50):
    a=n*0.50
    
elif(n>50 and n<=150):
    n=n-50
    a=25+n*0.75
elif(n>150 and n<=250):
    n=n-150
    a=100+n*1.20
elif(n>250):
    n=n-250
    a=220+n*1.50
print("Total bill is ",a)