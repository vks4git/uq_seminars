from flask import Flask
from flask import jsonify
from flask import request
import pymongo

myclient = pymongo.MongoClient("mongodb://mongodb:27017/")
mydb = myclient["seminars"]
mycol = mydb["data"]
app = Flask(__name__)

@app.route('/query/', methods=['GET'])
def query():
    args = request.args.to_dict()
    mydoc = list(mycol.find(args))
    for d in mydoc:
        d["_id"] = str(d["_id"])
    print(mydoc)
    response = { "count": len(mydoc), "data": mydoc }
    return jsonify({"response": response})

@app.route('/add/', methods=['GET'])
def add():
    args = request.args.to_dict()
    x = mycol.insert_one(args)
    return jsonify({"Inserted with ID": str(x.inserted_id)})

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

def run():
    app.run(host='0.0.0.0', port=3000, threaded=True)
