#encoding=utf-8

from flask import Flask
from flask import request
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.debug = True
app.use_debugger = True

@app.route("/")
def index():
    req = requests.get('http://git.xici.com/api/v3/projects/chekun%2fflask-dances-with-gitlab/repository/branches?private_token=xxx')
    result = req.json()
    options = [u'<option value="%s">%s</option>' % (branch['name'], branch['name']) for branch in result]
    return u'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Preview 分支管理</title>
        </head>
        <body>
            <h3>Preview 分支管理</h3>
            <form method="post" action="/checkout" charset="utf-8">
                <p>
                    分支:
                    <select name="branch">
                        %s
                    </select>
                </p>
                <p>
                    <input type="submit" value="切换分支" />
                </p>
            </form>
        </body>
    </html>
    ''' % (''.join(options))

@app.route("/checkout", methods=["post"])
def checkout():
    return '''
    %s <a href="javascript:history.back(-1)">返回</a>
    ''' % request.form['branch']

if __name__ == "__main__":
    app.run(host='0.0.0.0')
