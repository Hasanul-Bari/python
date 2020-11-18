fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1



bigcount=None
bigword=None

for word,count in counts.items():
    if bigcount is None or bigcount<count:
        bigcount=count
        bigword=word


print(bigword, bigcount)
