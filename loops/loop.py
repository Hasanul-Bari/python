n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff')
print(n)


#break continue
print('-------------------------')
while True:
    line=input('> ')

    if line[0]=='#':
        continue
    if line=='Done':
        break
    print(line)
print('Done!')



print('---------------------for loops----------------')
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff')


print('------------for string----------------')
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
