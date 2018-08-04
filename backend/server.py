from flask import request,jsonify


from flask import Flask
from Setup import Setup



app = Flask(__name__)
s = Setup()
@app.route('/')
def index():return 'Hola! IIM'

@app.route('/getSetup')
def getSetup():
    res = s.getOfficialWebsite(request.args.get('q'))
    #print(res)
    return(jsonify(res))

if __name__ == "__main__":
    app.run()
