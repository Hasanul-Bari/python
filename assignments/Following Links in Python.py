import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors        // enable to look https websites
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter - ')                                      #http://py4e-data.dr-chuck.net/known_by_Hajra.html
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')



#retrive anchor tags
i=input('Enter Count - ')              # 7
pos=input('Enter Position- ')          #18
i=int(i)
pos=int(pos)

while i>0:
    tags=soup('a')
    j=0
    for tag in tags:
        j=j+1
        if j==pos:
            url=tag.get('href',None)
            content=tag.contents[0]
            #print(content)
            html=urllib.request.urlopen(url, context=ctx).read()
            soup=BeautifulSoup(html, 'html.parser')
            break
    
    i=i-1
    
print(content)  # starts with R
