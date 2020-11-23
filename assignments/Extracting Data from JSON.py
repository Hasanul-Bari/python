import urllib.request, urllib.parse, urllib.error
import ssl
import json


#ignore SSL certificate errors        
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url=input('Enter - ')                                          #http://py4e-data.dr-chuck.net/comments_1060374.json          
data=urllib.request.urlopen(url, context=ctx).read()
info=json.loads(data)

s=0
for item in info['comments'] :
    #print(item['count'])
    val=item['count']
    s=s+int(val)
    
print(s)
