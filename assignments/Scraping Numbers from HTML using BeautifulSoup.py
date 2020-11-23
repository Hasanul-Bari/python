import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors        // enable to look https websites
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter - ')                                    #http://py4e-data.dr-chuck.net/comments_42.html
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')



#print(soup)

spans=soup('span')
sum=0
for span in spans:
    #print(span.contents[0])
    content=span.contents[0]
    sum=sum+int(content)
    
print(sum)
    
    
