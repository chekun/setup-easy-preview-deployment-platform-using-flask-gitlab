#encoding=utf-8

import json

json_string = '''
{
    "key": "value",
    "list": [
        {
            "k1": "value1"
        },
        {
            "k2": 2
        },
        {
            "k3": true
        }
    ]
}
'''

jsonObject = json.loads(json_string)

print json_string
print jsonObject
print jsonObject["key"]
print jsonObject["list"][2]["k3"]
