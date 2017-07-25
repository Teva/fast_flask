#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, webbrowser


#Directory to be created
parent = raw_input("where do you want to have you flask application installed : ")
child = parent+"/"+"app"
child0_1 = child+"/"+"static"
child0_2 = child+"/"+"templates"

#Directory container
dir_elm = [parent,child, child0_1, child0_2]

#files to be created
files_var = ["index.html","layout.html","login.html"]
static_files = ["styles.css"]

def init_file(directory):
    file = open(directory+'/'+'__init__.py','w')
    file.write('from flask import Flask\n')
    file.write('app = Flask(__name__)\n')
    file.write('from app import views')
    file.close()

def run_file(directory):
    file = open(directory+'/'+'run.py','w')
    file.write('from app import app \n')
    file.write('app.run(debug=True) \n')
    file.close()

def views_file(directory):
    file = open(directory+'/'+'views.py','w')
    file.write('from app import app \n')
    file.write('@app.route("/") \n')
    file.write('@app.route("/index") \n')
    file.write('def index():\n')
    file.write('    return "Hello, World!"')
    file.close()

def create_file(directory,filename):
    file = open(directory+'/'+filename,'w')
    file.close()

for elm in dir_elm:
    if not os.path.exists(elm):
        os.makedirs(elm)

for elm in dir_elm:
    if elm == dir_elm[0]:
        run_file(elm)
    elif elm == dir_elm[1]:
        init_file(elm)
        views_file(elm)
    elif elm == dir_elm[2]:
        for val in static_files:
            create_file(elm, val)
    elif elm == dir_elm[3]:
        for val in files_var:
            create_file(elm, val)


os.system("chmod a+x "+parent+'/'+"run.py")
os.system("python "+parent+'/'+"run.py")
new = 2
url = "http://127.0.0.1:5000"
webbrowser.open(url, new=new)


# /Volumes/Transcend/Test/
