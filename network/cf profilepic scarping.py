import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#ignore SSL certificate errors        // enable to look https websites
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter - ')
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')



#retrive anchor tags
tags=soup('img')
for tag in tags:
    
    #print('TAG:', tag)
    #print('URL:', tag.get('src', None))
    url=tag.get('src', None)
    if re.search('^//userpic.codeforces.com',url):
        print(url)
        img=html=urllib.request.urlopen('http:'+url, context=ctx).read()
        fhand = open('profilepic.jpg', 'wb')
        fhand.write(img)
        fhand.close()
    
