from flask import Flask, request
import json


app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def hello():

    if request.method == 'POST':
        resp = json.dumps({'dataset': 'D1', 'tr_setup': 'set1', 'results': 1})
    
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
