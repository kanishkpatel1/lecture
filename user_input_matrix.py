from numpy import*
r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))
str=input("Enter matrix elements with space:\n") #accept matrix element as a string into str
#convert the string into a matrix wit size that user input(r x c)
x=reshape(matrix(str),(r,c))
print(x)
