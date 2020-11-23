import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET


#ignore SSL certificate errors        
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url=input('Enter - ')                                          #http://py4e-data.dr-chuck.net/comments_1060373.xml          
data=urllib.request.urlopen(url, context=ctx).read()
commentinfo=ET.fromstring(data)
lst=commentinfo.findall('comments/comment')

s=0
for item in lst:
    #print(item.find('count').text)
    val=item.find('count').text
    s=s+int(val)
    
print(s)
