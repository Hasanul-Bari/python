import re

fhand=open('input.txt')

for line in fhand:
    line=line.strip()

    if re.search('From:',line):
        print(line)


#matches start with
print('-----------------------------------------------------------------')
fhand=open('input.txt')

for line in fhand:
    line=line.strip()

    if re.search('^From:',line):
        print(line)


#starts with X follewed by any no. if char, followed by :
print('-----------------------------------------------------------------')
fhand=open('input.txt')

for line in fhand:
    line=line.strip()

    if re.search('^X.*:',line):
        print(line)


#starts with X- follewed by one or more  nonwhitespace if char, followed by :
#X-Sieve: CMU Sieve 2.3           true
#X-DSPAM-Result: Innocent         true
#X-: Very Short                   false
#X-Plane is behind schedule: two weeks      false

print('-----------------------------------------------------------------')
fhand=open('input.txt')

for line in fhand:
    line=line.strip()

    if re.search('^X-\S+:',line):
        print(line)
