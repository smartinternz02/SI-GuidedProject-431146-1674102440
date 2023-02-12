# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

md = pickle.load(open("price.pkl","rb"))
sc = pickle.load(open("scale.pkl","rb"))
@app.route('/')
def hello_world():
    return render_template("value.html")
@app.route('/home')
def home():
         return render_template('value.html')
@app.route('/value',methods = ["POST"])
def value():
    p = request.form["a"]
    q= request.form["b"]
    r = request.form["c"]
    s = request.form["d"]
    t = request.form["e"]
    u = request.form["f"]
    data = [[p,q,r,s,t,u]]
    dt=(sc.fit_transform(data))
    prd=md.predict(dt)
    return render_template("value.html",y=prd)
app.run(debug = True)