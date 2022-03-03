print("find Even odd using if else\n ")
a=int(input("Enter a number that you want to check: "))
if(a%2==0):
    print(a,"is Even")
else:
    print(a," is Odd")
print("find Even odd using if bitwise")
a=int(input("Enter a number that you want to check: "))
if(a&1):
    print(a,"is Odd  number ")
else:
    print(a,"is Even number")