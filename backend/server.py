from flask import request,jsonify
from flask import Flask
from flask_cors import CORS

from Setup import Setup
from Wiki import Wiki
from Stackoverflow import Stackoverflow
from Intent import Intent

app = Flask(__name__)
CORS(app)

setup = Setup()
info = Wiki()
tags = Stackoverflow()
intent = Intent()

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
    try:
        req = request.args.get('q').replace("+"," ")
        print(req)
        adj = intent.getIntent(req)
        if adj == 'error':
            adj = req
        infoResponse = info.getInfo(adj)
        tagsResponse = tags.getRelatedTags(adj)
        setupResponse = setup.getOfficialWebsite(adj)
        response['info'] = infoResponse
        response['tags'] = tagsResponse
        response['setup'] = setupResponse
    except Exception:
        response['info'] = "Some error occurred... Please try again later"
        response['tags'] = "Some error occurred... Please try again later"
        response['setup'] = "Some error occurred... Please try again later"
    return(jsonify(response))

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
