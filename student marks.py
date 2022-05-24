from array import*
str=input("Enter marks in all subject with space:").split()
print(str) #this [will ] print string list
marks =[int(num) for num in str]  #it convernt from string to integer
print(marks)

total=sum(marks)
print(total,"marks get the strudent")