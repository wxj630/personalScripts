# -*- coding: utf-8 -*-

"""
@author: wuxiaojun

@contact: wuxiaojun@cetccity.com

@software: PyCharm

@froject name: personalScripts

@file: app.py

@time: 2020/7/24  11:18 

@desc: 待定
"""
from flask import Flask,redirect,session,url_for,request,abort,make_response
from flask import jsonify
app = Flask(__name__)
app.secret_key = 'wxj011289'

@app.route('/')
def index():
    return '<h1>Hello Flask</h1><h6>edited by wuxiaojun'

@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name',name)
    return response

# @app.route('/login/<string:name>')
# def login(name):
@app.route('/login')
def login():
    session['logged_in'] = True
    # session['name'] = name
    return redirect(url_for('hello'))

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','Human') # session就是加密的cookie
        # name = session['name'] if session['name'] is not None else 'Human'
        response = '<h1>hello, %s！</h1>' % name

    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response

@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return '<h1>Welcome to admin page.</h1>'

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
        # session.pop('name')
    return redirect(url_for('hello'))

@app.route('/show')
def show():
    datas = {}
    id = 0
    lines = ''
    with open('data.csv',encoding='utf-8') as f:
        for line in f.readlines():
            author = str(line.split(',')[0])
            title = str(line.split(',')[1])
            article = str(line.split(',')[2])
            print(author)

            data = {}
            data['author'] = author
            data['title'] = title
            data['article'] = article

            datas[id] = data

            id += 1

            lines = lines + '\n' + line


    return lines

