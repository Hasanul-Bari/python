purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75

print(purse)
print(purse['candy'])
purse['candy']=purse['candy']+2
print(purse)


eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

print('candy' in purse)
print('pen' in purse)

print(purse.get('candy',0))
print(purse.get('pen',0))         #na thakle default value 0


for key in purse:
    print(key,purse[key])

for k,v in purse.items():
    print(k,v)                  #two iteration variable
