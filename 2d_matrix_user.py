from numpy import*
(a,b)=map(int,input('Enter the value of rows and columns:').split())
#for matrix 1
str1=input("Enter the first matrix elements:")  #separated with space ex--1 2 3 4 
x=reshape(matrix(str1),(a,b))
print("matrix 1=",x)
#for matrix 2
str2=input("Enter the second  matrix elements:")  #separated with space ex=1 2 3 4 
y=reshape(matrix(str2),(a,b))
print("matrix 2=",y)


a=x+y  #addition of both matrix
b=x*y   #multiplication of both matrix
print("addition of matrix is",a)  
print("multiplication of matrix is",b)


y=transpose(x) #transpose matrix
print("transpose matrix of x ",y)

