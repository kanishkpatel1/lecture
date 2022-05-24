from array import*
a=array('i',[10,20,30,40,50])
print( "original array : ",a)

a.append(30)
a.append(60)
print("array after appending:  ",a)

a.insert(1,99)
print("array after inserting element 99 at position  1 : ",a)

a.remove(20)
print("array after remove 20 : ",a)

arr=a.pop()  # it give last element
print("array after using pop () : ",a)
print("pooped element : ",arr)

arr=a.index(30)
print("First occurance of element 30 is at index ",arr)


# converting array  into a list
lst=a.tolist()
print("array : ",a)
print("list : ",lst)

print("array is : ",a)
a.reverse()  # for reverse array 
print("array in reverse order : ",a)

