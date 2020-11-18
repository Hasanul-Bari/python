# Use words.txt as the file name
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


for line in fhand:
    line=line.rstrip()
    print(line.upper())
