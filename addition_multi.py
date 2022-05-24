from numpy import*
r=int(input("Enter the number of rows:")) #in this program we give row and column of both matrix is same
c=int(input("Enter the number of columns:"))
str1=input("Enter matrix 1 elements with space:\n") #accept matrix element as a string into str
#convert the string into a matrix wit size that user input(r x c)
m1=reshape(matrix(str1),(r,c))

#2nd matrix user input
str2=input("Enter matrix 1 elements with space:\n") #accept matrix element as a string into str
#convert the string into a matrix wit size that user input(r x c)
m2=reshape(matrix(str2),(r,c))

#displaying both matrix
print("matrix 1:\n")
print(m1)
print("matrix :2\n:")
print(m2)

#sum
print("sum of both matrix:\n")
print(m1+m2)

#product of both the matrix
print("product of both the matrix:\n")
p=m1*m2
print(p)
