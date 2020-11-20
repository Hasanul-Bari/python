import json

data='''
{
    "name" : "Hasan",
    "phone": {
                "type" : "intl",
                "number" :"01521427065"
    },
    "email" : {
                "hide" : "yes"
    }
}'''
        
        
        
info=json.loads(data)

print('Name:', info['name'])
print('Hide:', info['email']['hide'])