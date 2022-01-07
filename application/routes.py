from application import app

from flask import render_template, request, redirect, url_for
import json
from json import JSONDecodeError
import os.path

jsonFileName = 'CameraSettings.json'

@app.route('/', methods=['GET','POST'])
def home():
    if os.path.exists( jsonFileName ):
        jsonFilePtr = open( jsonFileName ) 
        try:
            settings = json.load( jsonFilePtr )
        except JSONDecodeError as err:
            print("JSON decoding err: ", err.msg)
            print("JSON Line #: ", err.lineno, ", Column #: ", err.colno)
        jsonFilePtr.close()
        return render_template("index.html", current=str(settings["current"]), increment=str(settings['increment']))
    else:
        return render_template("index.html")
    
@app.route('/camera', methods=['GET','POST'])
def camera():
    if request.method == 'POST':
        increment = request.form['increment']
        current = request.form['current']             
        settings =  {
                        "increment": increment, 
                        "current": current
                    }

        prusa = open( jsonFileName, 'w' )
        json.dump( settings, prusa, indent=4 )

        if request.form['buttonName'] == 'Reset':
            print("Reset")
            increment = 0
            current = 0
            return render_template( "index.html", current=str(current), increment=str(increment) )

        elif request.form['buttonName'] == 'Left':
            print("Go Left")

        elif request.form['buttonName'] == 'Right':
            print("Go Right")

        elif request.form['buttonName'] == 'Take Picture':
            print("Take Picture")

        return redirect( url_for("home") )

    else:
        return redirect( url_for("home") )