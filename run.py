#-*- coding:utf-8 -*-
from flask import Flask,url_for,abort,make_response
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index/')
def index():
    import subprocess,chardet
    cmd = subprocess.Popen(['tasklist'],stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
    out,error = cmd.communicate()
    out=out.decode('gbk','ignore').encode('utf-8')
    memory = out.splitlines()
    
    return render_template('index.html', memory=memory,error=error)

@app.route('/login')
def login():
    pass

@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

with app.test_request_context():
    print url_for('index')
    print url_for("login")
    print url_for("login",next='/')
   

if __name__ == '__main__':
    app.debug = True
    app.run()
    