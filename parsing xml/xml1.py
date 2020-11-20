import xml.etree.ElementTree as ET

data='''
<person>
    <name>Hasan</name>
    <phone type="intl">
        01521427065
    </phone>
    <email hide="yes"/>
</person>'''


tree=ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
print('Attr: ', tree.find('phone').get('type'))