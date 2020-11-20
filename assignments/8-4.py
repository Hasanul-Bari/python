fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

ans = list()

for line in fhand:
    list=line.split()

    for word in list:
        if word not in ans:
            ans.append(word)

ans.sort()
print(ans)
