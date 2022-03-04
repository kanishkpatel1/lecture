s=int(input("Enter your basic salary : "))
if(s<10000):
    hra=(s*80)//100
    da=(s*90)//100
elif(s>10000 and s<=20000):
    hra=(s*85)//100
    da=(s*90)//100
elif(s>20000):
    hra=(s*95)//100
    da=(s*95)//100
t=da+hra
print("Your total salary is ",t)