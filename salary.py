s=int(input("Enter your basic salary : "))
if(s<=10000):
    hra=(s*80)//100
    da=(s*90)//100
    print("Your total salary is ",hra+da+s)
if(s>10000 and s<=20000):
    hra=(s*85)//100
    da=(s*90)//100
    print("Your total salary is ",hra+da+s)
if(s>20000):
    hra=(s*95)//100
    da=(s*95)//100
    print("Your total salary is ",hra+da+s)
