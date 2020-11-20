fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

c=0
for line in fhand:
    if not line.startswith("From ") :
        continue

    list=line.split()
    print(list[1])
    c=c+1


print("There were", c, "lines in the file with From as the first word")
