import sqlite3

conn=sqlite3.connect('emaildb.sqlite')
curs=conn.cursor()

curs.execute('DROP TABLE IF EXISTS Counts')
curs.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
        
    pieces = line.split()
    email = pieces[1]
    print(email)
    
    curs.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = curs.fetchone()
    
    if row is None:
        curs.execute('''INSERT INTO Counts (email, count)
                    VALUES (?, 1)''', (email,))
    else:
        curs.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))
    
    conn.commit()
    
    
#read table from db 
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in curs.execute(sqlstr):
    print(str(row[0]), row[1],)

curs.close()