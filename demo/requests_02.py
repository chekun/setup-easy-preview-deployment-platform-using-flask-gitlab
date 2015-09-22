#encoding=utf-8

import os
import requests

req = requests.get('http://git.xici.com/api/v3/projects/chekun%2fflask-dances-with-gitlab/repository/branches?private_token=xxx')

result = req.json()

if req.status_code != 200:
    print result['message']
    os.exit(-1)

print 'Branches of chekun/flask-dances-with-gitlab\n'

for branch in result:
    print '* %s' % (branch['name'])

print '\n'
