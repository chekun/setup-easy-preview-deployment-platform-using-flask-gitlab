#encoding=utf-8

from flask import Flask
from flask import request
import requests
import sys
import subprocess

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.debug = True
app.use_debugger = True

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html style="height:100%%;width:100%%;">
        <head>
            <meta charset="utf-8">
            <title>Python Runner</title>
            <link rel="stylesheet" href="http://www.bootcss.com/p/buttons/css/buttons.css">
        </head>
        <body style="position:relative;height:100%%;margin:0">
            <div style="position:absolute;top: 35%%;left:45%%">
                <a href="/run?s=%s" class="button button-action button-pill button-jumbo">Run</a>
            </div>
        </body>
    </html>
    ''' % request.args.get('s')

@app.route('/redirector')
def redirect():
    url = request.args.get('url', '')
    return u'''
    <!DOCTYPE html>
    <html style="height:100%%;width:100%%">
        <head>
            <meta charset="utf-8">
            <title>Python Runner</title>
            <link rel="stylesheet" href="http://www.bootcss.com/p/buttons/css/buttons.css">
        </head>
        <body style="position:relative;height:100%%;margin:0">
            <div style="position:absolute;top: 35%%;left:45%%">
                <a href="%s" class="button button-royal button-pill button-jumbo">Visit</a>
            </div>
        </body>
    </html>
    ''' % url

@app.route('/run')
def run():

    cmd = "docker rm -f $(docker ps -aq)"
    subprocess.call(cmd, shell=True)

    volumn = '/Users/chekun/Work/xici/share/flask-gitlab/'

    cmd = "docker run -d -p 5000:5000 -p 5001:5001 -v %s:/demo chekun/flask-gitlab" % volumn
    output = subprocess.check_output(cmd, shell=True)
    containerId = output.replace('\n', '')
    if 'server' in request.args.get('s'):
        cmd = "docker exec %s python /demo/demo/%s.py" % (containerId, request.args.get('s'))
        subprocess.Popen(cmd, shell=True)
        cmd = "docker logs %s" % containerId
        output = subprocess.check_output(cmd, shell=True)
    else:
        cmd = "docker exec %s python /demo/demo/%s.py" % (containerId, request.args.get('s'))
        output = subprocess.check_output(cmd, shell=True)
    console = ''.join(['<p><a></a>%s</p>' % line for line in output.split('\n')])

    return '''
    <!DOCTYPE html>
    <html style="height:100%%;width:100%%;">
        <head>
            <meta charset="utf-8">
            <title>Python Runner</title>
            <link rel="stylesheet" href="http://cdn.staticfile.org/normalize/3.0.1/normalize.min.css">
            <link rel="stylesheet" href="http://7fvdgt.com1.z0.glb.clouddn.com/terminal.css">
            <style>
                p {-webkit-margin-before: 0em;-webkit-margin-after: 0em;min-height: 18px;}
            </style>
        </head>
        <body style="margin:0;background-color: #2a2a2a;">
            <div id="log-container" class="terminal" style="margin-top:0">
                <div class="terminal-body">
                    <pre id="log" class="ansi" style="margin:0;line-height: 3px;">
                        %s
                    </pre>
                </div>
            </div>
        </body>
    </html>
    ''' % console

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
