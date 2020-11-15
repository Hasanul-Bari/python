str=input('Enter a number')

try:
    x=int(str)
except Exception as e:
    print(e)

print('End')


str=input('Enter a number')

# another example

try:
    x=int(str)
except:
    x=-1

if x>0:
    print('Nice work')
else:
    print('Not a number')
