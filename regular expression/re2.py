#find all the matches and return a list
#[0-9]+  one or more digit
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
#one or more uppercase vowel
y = re.findall('[AEIOU]+',x)
print(y)


#greedy matching: matches the largest  possible string
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

#non greedy
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
['From:']


#extract email : one or more non-blank char followed by one or more non-blank char
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print(y)

#Parentheses are not part of the match - but they tell where to start and stop what string to extract
y = re.findall('^From (\S+@\S+)',x)
print(y)



#Extracting a host name
y = re.findall('@([^ ]*)',x)
print(y)


#Extracting a host name  : check line with from
y = re.findall('^From .*@([^ ]*)',x)
print(y)



#If you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)
