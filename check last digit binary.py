# write a python program to check wether last digit is binary or not
a=int(input("Enter the number that you want to check : "))
n=a%10
b=n&1
print("Last binary digit is ",b)