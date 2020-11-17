fhand=open('input.txt','r')

print(fhand)


#for line in fhand:
#    print(line)


#count line no
count=0
for line in fhand:
    count = count + 1
print('Line Count:', count)


#getting the full file into string
fhand=open('input.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])


#search through Files
fhand=open('input.txt')
for line in fhand:
    line=line.rstrip()                 # file theke je \n thake remove kre, karon print abar /n dey
    if line.startswith('From:'):
        print(line)

print('----------------------------------')
fhand=open('input.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)




#Letting the user choose the file name
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
