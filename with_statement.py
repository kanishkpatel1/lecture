with open('1.txt','w+') as f: #write the data with statement

    f.write("rahul is my friend\n")
    f.write("he is from bihar\n")

# for reading the data
    f.seek(0,0)
    for line in f:
        print(line)