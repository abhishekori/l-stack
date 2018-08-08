from flask import request,jsonify
from flask import Flask
from flask_cors import CORS

import threading

from Setup import Setup
from Wiki import Wiki
from Stackoverflow import Stackoverflow
from Intent import Intent
from MOOC import MOOC
from HelloWorld import HelloWorld
from Suggestions import Suggestions

app = Flask(__name__)
CORS(app)

setup = Setup()
info = Wiki()
tags = Stackoverflow()
intent = Intent()
mooc = MOOC()
helloworld = HelloWorld()
suggestions = Suggestions()

@app.route('/')
def index():return 'Hola! IIM'

'''
@app.route('/getSetup')
def getSetup():
    res = setup.getOfficialWebsite(request.args.get('q'))
    return(jsonify(res))

@app.route('/getInfo')
def getInfo():
    res = info.getInfo(request.args.get('q'))
    return(jsonify(res))

@app.route('/getTags')
def getTags():
    res = tags.getRelatedTags(request.args.get('q'))
    return(jsonify(res))


@app.route('/getSuggestions')
def getSuggestions():
    req = request.args.get('q').replace("+"," ")
    suggestionsResponse = suggestions.getSuggestions(req)
    return(jsonify(suggestionsResponse))

@app.route('/getIntent')
def getIntent():
        req = request.args.get('q').replace("+"," ")
        print(req)
        adj = intent.getIntent(req)
        if adj == 'error':
            adj = req
        return adj

'''

@app.route('/summary')
def summary():
    response = {}
    adj = ""
    req = request.args.get('q').replace("+"," ")

    thread1 = threading.Thread(target = intent.getIntent , args = (req,response,))
    thread1.start()
    thread1.join()
    adj = response.get('intent')

    try:
        thread2 = threading.Thread(target =  info.getInfo, args = (adj,response,))
    except Exception:
        response['info'] = "Some error occurred... Please try again later"

    try:
        thread3 = threading.Thread(target =  tags.getRelatedTags, args = (adj,response,))
    except Exception:
        response['tags'] = "Some error occurred... Please try again later"

    try:
        thread4 = threading.Thread(target =  setup.getOfficialWebsite, args = (adj,response,))
    except Exception:
        response['setup'] = "Some error occurred... Please try again later"

    try:
        thread5 = threading.Thread(target =  mooc.getMoocs, args = (adj,response,))
    except Exception:
        response['moocs'] = "Some error occurred... Please try again later"

    try:
        thread6 = threading.Thread(target =  helloworld.getHelloWorlds, args = (adj,response,))
    except Exception:
        response['helloworlds'] = "Some error occurred... Please try again later"

    try:
        thread7 = threading.Thread(target =  suggestions.getSuggestions, args = (req,response,))
    except Exception:
        response['suggestions'] = "Some error occurred... Please try again later"

    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()

    return(jsonify(response))

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = True)
