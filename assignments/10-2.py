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
    time=list[5]
    time=time.split(':')
    hr=time[0]
    #print(hr)
    freq[hr]=freq.get(hr,0)+1


for k,v in sorted(freq.items()):
    print(k,v)
