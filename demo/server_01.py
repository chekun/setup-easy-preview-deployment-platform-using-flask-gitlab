#encoding=utf-8

from flask import Flask
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

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
            <form method="post">
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
