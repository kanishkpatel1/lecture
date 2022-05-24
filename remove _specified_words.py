a=["red","orange","yellow","green","white","black"]
b=["red","yellow"]  #remove these words from list a
y=list(filter(lambda a:a not in b ,a))
print(y)