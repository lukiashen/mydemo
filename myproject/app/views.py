from flask import render_template
from flask import Flask, jsonify, render_template, request,Response
from app import app
import pymongo 
import bson.binary 
import json
import string
import random
from cStringIO import StringIO 
from datetime import datetime
from flask import Flask
from flask import g
from flask import jsonify
from flask import json
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask import make_response
import pymongo
from pymongo import Connection
from bson import BSON
from bson import json_util
db = pymongo.MongoClient('localhost', 27017).test 

@app.route('/')
@app.route('/index')


def index():
    #db.users.remove()
    return render_template("index.html")
@app.route('/register')
def register():


	return render_template("register.html")
@app.route('/login')
def login():
	return render_template("login.html")
@app.route('/ConfirmUsers')
def confirmusers():
	name=request.args.get('name')
	passwd=request.args.get('passwd')
	print name
	print passwd
	b=db.users.find({"username":name,"passwd":passwd})
	if (b.count()!=0):
		str={"result":1}
		return Response(json.dumps(str))
	else:
		str={"result":0}
		return Response(json.dumps(str))

@app.route('/loginsucceed')
def loginsucceed():
   
	return render_template("loginsucceed.html")
@app.route('/reg')
def reg():
	name=request.args.get('name')
	passwd=request.args.get('passwd')
	db.users.insert({"username":name,"passwd":passwd})

	return Response()
@app.route('/getUsers')

def getuser():
	doc=list(db.users.find())
	length=len(doc)
	#print doc
	print length
	jsondata={"doc":doc,"len":length}
	myjson=json.dumps(jsondata,default=json_util.default)
	return Response(myjson)
@app.route('/delusers')

def delusers():
	name=request.args.get('name')
	word=name.split('#')
	i=0;
	while word[i]!='':
		print word[i]
		db.users.remove({"username":word[i]})
		i=i+1
	
	return Response()
@app.route('/resetpwd')

def resetpwd(minlength=5,maxlength=25):
	name=request.args.get('name')
	length=random.randint(minlength,maxlength)
	letters=string.ascii_letters+string.digits
	newpwd=''.join([random.choice(letters) for _ in range(length)]) 
	print newpwd
	db.users.update({"username":name},{"$set":{"passwd":newpwd}})
		
	
	return Response()




    