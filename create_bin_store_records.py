reclen=20  #take the record size as 20 bytes

with open('cities.bin','wb') as f: #open the file as wb mode because the file is bin type
    n=int(input("HOw many entries?:"))
    for i in range(n):
        city=input("Enter city name:")
        ln=len(city)
        city =city+(reclen-ln)*' '  #increase the city name to 20 chars by adding remaining spaces
        city=city.encode() #CONVERT the city name into byte string
        f.write(city)