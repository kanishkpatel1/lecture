reclen=20
with open('cities.bin','rb') as f:
    n=int(input("Enter the record number:"))
    f.seek(reclen*(n-1))
    str=f.read()
    print(str.decode())