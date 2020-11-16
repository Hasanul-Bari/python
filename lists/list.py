print([1,24,76])
print(['red','yello','blue'])
print(['red',24,98,6])
print([1, [5,6], 6])
print([])




friends=['Hasan','Hasanul', 'Hasanul Bari']
for friend in friends:
    print('Hello', friend)
print('Done')

print(friends[1])


#Lists are mutable
numbers = [17, 123]
numbers[1] = 5
print(numbers)

print(len(friends))

#range function
print(range(4))
print(range(len(friends)))


for i in range(len(friends)):
    friend=friends[i]
    print('Hello', friend)



print('---------------List operations------------------')
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print([0] * 4)


print('---------------List methods------------------')
x=list()
print(type(x))
print(dir(x))


#is something in List
some=[1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

print(some)
some.sort()
print('After sort: ', some)

print('length:', len(some))
print('Max:',max(some))
print('Min:',min(some))
print('Sum:',sum(some))
print('Avg:',sum(some)/len(some))


#delete elements
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

t = ['a', 'b', 'c']
del t[1]
print(t)


t = ['a', 'b', 'c']
t.remove('b')
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)
