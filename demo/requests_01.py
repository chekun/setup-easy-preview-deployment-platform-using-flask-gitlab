#encoding=utf-8

import requests

req = requests.get('http://git.xici.com/api/v3/projects/chekun%2fflask-dances-with-gitlab/repository/branches')

print req.text

result = req.json()

print result

if req.status_code != 200:
    print result['message']

print '请求成功!'
