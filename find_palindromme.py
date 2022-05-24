lst=['php','w3r','mom','sas','ass']
a=list(filter(lambda x: x==x[-1: :-1],lst))
print(a)