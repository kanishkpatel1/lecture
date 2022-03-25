n=input("Enter the string: ")
a=len(n)
n1=int(input("Enter the number of characters to capitalize: "))
print(n[0:a-n1] +n[a-n1:].upper())