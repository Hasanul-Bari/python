fruit='banana'
print(fruit[1])

print(len(fruit))

for l in fruit:
    print(l)


#slicing string
s='Monty python'
print(s[0:4])     #range is upto not including
print(s[6:7])
print(s[6:20])    #ok no traceback



print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit:
    print('Found it')



#String comparison
word='Pineapple'
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')





greet='Hello Hasan'
print(greet.lower())
print(type(greet))
print('Methods : ----------')
print(dir(greet))



print(fruit.find('na'))
print(fruit.find('z'))  #not present then -1 if  present then index



#replace
print(greet.replace('Hasan','Hasanul'))
print(greet.replace('a','X'))


#striping whitespace
line = '  Here we go  '
print(line.lstrip())
print(line.rstrip())
print(line.strip())


#prefixes
line = 'Have a nice day'
print(line.startswith('Have'))
print(line.startswith('h'))



#parsing and extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)
