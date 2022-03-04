#  enter the input 301 for correct answer
a=int(input("Enter the number of apples : "))
if(a%7==0 and a%6==1 and a%5==1 and a%4==1 and a%3==1 and a%2==1):
    print("Entered number is correct")
else:
    print("Pls Enter correct number")