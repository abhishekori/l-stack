from flask import request,jsonify
from flask import Flask
from flask_cors import CORS

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


@app.route('/summary')
def summary():
    response = {}
    adj = ""
    req = request.args.get('q').replace("+"," ")
    adj = intent.getIntent(req)
    if adj == 'error':
        adj = req

    response['intent'] = adj

    try:
        infoResponse = info.getInfo(adj)
        response['info'] = infoResponse
    except Exception:
        response['info'] = "Some error occurred... Please try again later"

    try:
        tagsResponse = tags.getRelatedTags(adj)
        response['tags'] = tagsResponse
    except Exception:
        response['tags'] = "Some error occurred... Please try again later"

    try:
        setupResponse = setup.getOfficialWebsite(adj)
        response['setup'] = setupResponse
    except Exception:
        response['setup'] = "Some error occurred... Please try again later"

    try:
        moocResponse = mooc.getMoocs(adj)
        response['moocs'] = moocResponse
    except Exception:
        response['moocs'] = "Some error occurred... Please try again later"

    try:
        helloworldResponse = helloworld.getHelloWorlds(adj)
        response['helloworlds'] = helloworldResponse
    except Exception:
        response['helloworlds'] = "Some error occurred... Please try again later"

    try:
        suggestionsResponse = suggestions.getSuggestions(req)
        response['suggestions'] = suggestionsResponse
    except Exception:
        response['suggestions'] = "Some error occurred... Please try again later"

    return(jsonify(response))

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
