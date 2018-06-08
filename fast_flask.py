#!/usr/bin/env python
# -*- coding: utf-8 -*-
# authors : Teva DELAR, Emmario DELAR

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
    """Creates the __init__.py file & adds the necessary variables :
    
    from flask import Flask
    from app import views
    """
    file = open(directory+'/'+'__init__.py','w')
    file.write('from flask import Flask\n')
    file.write('app = Flask(__name__)\n')
    file.write('from app import views')
    file.close()

def run_file(directory):
    """Creates the run.py file & adds the necessary variables :
    
    from app import app
    app.run(debug=True)
    """
    file = open(directory+'/'+'run.py','w')
    file.write('from app import app \n')
    file.write('app.run(debug=True) \n')
    file.close()

def views_file(directory):
    """Creates the views.py file & adds the necessary variables :
    
    from app import app
    @app.route("/")
    @app.route("/index")
    def index():
        return "Hello, World!
    """
    file = open(directory+'/'+'views.py','w')
    file.write('from app import app \n')
    file.write('@app.route("/") \n')
    file.write('@app.route("/index") \n')
    file.write('def index():\n')
    file.write('    return "Hello, World!"')
    file.close()

def create_file(directory,filename):
    """This function will be used to create directory tree and the static html files
    """    
    file = open(directory+'/'+filename,'w')
    file.close()

#Execution starts here
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

#Command line access to run the current python file and access it via the localhost
os.system("chmod -R 777 "+dir_elm[0])
os.system("chown -R $USERNAME:$USERNAME "+dir_elm[0])
os.system("python "+parent+'/'+"run.py")
os.system("pip install flask")
new = 2
url = "http://127.0.0.1:5000"
webbrowser.open(url, new=new)
