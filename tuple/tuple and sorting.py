#top 10 frequent word

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


list=list()
for k,v in counts.items():
    list.append( (v,k) )       # append (value,key) tuple


list=sorted(list, reverse=True)    # sort in reverse according to value


for v,k in list[:10] :
    print(k , v)                      # top 10 key,value tuple


#another way:
print(sorted( [ (v,k) for k,v in counts.items()] ) )
