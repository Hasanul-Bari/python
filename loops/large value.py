largest = None
print('Before:', largest)
for num in [3, 41, 12, 9, 74, 15]:
    if largest is None:
        largest= num
    elif num>largest :
        largest = num
    print('Loop:', num, largest)
print('Largest:', largest)
