from flask import Flask, request
import json
import avalanche


app = Flask(__name__)


"Simple API to check if all ok with Flask microservices in deploy"
@app.route("/", methods=['GET'])
def hello():
    resp = json.dumps({'dataset': 'D1', 'tr_setup': 'set1', 'results': 1})
    
    return resp


"This is a simple API to test if avalanche is installed correctly."
@app.route("/avalanche", methods=['GET'])
def api_avalanche():
    avalanche_info = test_avalanche_setup()
    resp = json.dumps({"avalanche_info": avalanche_info})
    
    return resp


"""
Functions
"""
def test_avalanche_setup():
    print("Avalanche Version:", avalanche)
    print("Everything looks fine here :-)")

    return avalanche


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
