f=open('1.txt')
l=f.readlines() #if we print l it give list element with /n character to remove it we will use below lines code
l=[line.strip() for line in l]
print(l)
