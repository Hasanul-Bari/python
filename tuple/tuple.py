t = ('a', 'b', 'c', 'd', 'e')
print(t)
print(type(t))
print(dir(t))


(x,y)=(4,'fred')
print(y)
(a,b)=(99,98)
print(a)


#comparing tuples
print( (0,1,2)<(5,1,2) )
print( (0,1,2)<(5,1,2) )
print( ('Jones','Sally')<('Jones','Sam') )
print( ('Jones','Sally')>('Adams','Sam') )



#sorting dictionary
purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75

print(list(purse.items()))   # a list of tuples

for k,v in sorted(purse.items()):    # sort according the first value in tuple which is dict key
    print(k,v)



#sort by value
tmp=list();
for k,v in purse.items():
    tmp.append( (v,k) )
print(tmp)

tmp=sorted(tmp, reverse=True)   #sort in reverse .desc
print(tmp)
