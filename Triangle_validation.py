a=int(input("Enter the number of 1st side :"))
b=int(input("Enter the number of 2nd side :"))
c=int(input("Enter the number of 3rd side :"))
if(a+b>c or b+c>a or a+c>b):
    print("triangle is valid")
else:
    print("Triangle is not valid ")
