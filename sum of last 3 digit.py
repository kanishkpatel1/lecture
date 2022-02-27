# wite a program to find the sum of last 3 digit of university roll number
n=int(input("Enter your university roll number :"))
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
n=n//10
print("sum of last 3 digit of your university roll no is ",a+b+c)