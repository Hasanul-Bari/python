fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


freq=dict()
for line in fhand:
    if not line.startswith("From ") :
        continue

    list=line.split()
    freq[list[1]]=freq.get(list[1],0)+1


bigcount=None
bigmail=None
for mail,count in freq.items():
    if bigcount is None or bigcount<count:
        bigcount=count
        bigmail=mail



print(bigmail, bigcount)
