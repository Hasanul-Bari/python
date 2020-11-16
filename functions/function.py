def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()



#argument

def greet(lang):
    if lang=='es':
        print('Hola')
    elif lang=='br':
        print('Ola')
    else:
        print('Hello')


greet('en')
greet('es')
greet('br')


#return
def greet():
    return 'Hello'

print(greet(),'Hasan')



def addtwo(a,b):
    added=a+b
    return added

x=addtwo(2,5)
print(x)
