# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

s=0.0
c=0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    line=line.strip()
    pos=line.find(':')
    line=line[pos+2:]
    s=s+float(line)
    c=c+1
    #print(line[pos+2:])
print('Average spam confidence:',s/c)
