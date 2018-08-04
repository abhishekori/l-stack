from flask import request,jsonify
from flask import Flask
from flask_cors import CORS

from Setup import Setup
from Wiki import Wiki
from Stackoverflow import Stackoverflow

app = Flask(__name__)
CORS(app)

setup = Setup()
info = Wiki()
tags = Stackoverflow()


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

@app.route('/summary')
def summary():
    response = {}
    infoResponse = info.getInfo(request.args.get('q'))
    tagsResponse = tags.getRelatedTags(request.args.get('q'))
    setupResponse = setup.getOfficialWebsite(request.args.get('q'))
    response['info'] = infoResponse
    response['tags'] = tagsResponse
    response['setup'] = setupResponse
    return(jsonify(response))

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
