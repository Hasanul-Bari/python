import re

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

s=0
for line in fhand:
    line=line.strip()
    nums=re.findall('[0-9]+',line)
    for num in nums:
        s=s+int(num)


print(s)
