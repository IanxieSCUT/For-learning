# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 13:01:10 2018

@author: Administrator
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return'<h1>Hello,World!</h1>'

if __name__=='__main__':
    app.run(debug=True)
