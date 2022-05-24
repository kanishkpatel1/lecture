#14. Write a Python program to combine each line from first file with the 
#corresponding line in second file
with open('cp.txt') as fh1, open('cp1.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)
