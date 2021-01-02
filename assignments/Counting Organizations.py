import sqlite3

conn=sqlite3.connect('organizationdb.sqlite')
curs=conn.cursor()

curs.execute('DROP TABLE IF EXISTS Counts')
curs.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
        
    pieces = line.split()
    email = pieces[1]
    pieces=email.split('@')
    orgs=pieces[1]
    print(orgs)
    
    curs.execute('SELECT count FROM Counts WHERE org = ? ', (orgs,))
    row = curs.fetchone()
    
    if row is None:
        curs.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (orgs,))
    else:
        curs.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(orgs,))
    
    conn.commit()
    
    
#read table from db 
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in curs.execute(sqlstr):
    print(str(row[0]), row[1],)

curs.close()
    
    