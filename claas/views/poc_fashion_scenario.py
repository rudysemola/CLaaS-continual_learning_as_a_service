from flakon import JsonBlueprint
from flask import abort, jsonify, request

from claas.classes.exp_poc_fashion_scenario import ExperimentFashionScenario


fashion_scenario = JsonBlueprint('fashion_scenario', __name__)

"""
GLOBAL VAR
"""
EXPERIMENT = ExperimentFashionScenario()


"""
API - CLaaS (Fashion Scenario)
"""
#TODO

@fashion_scenario.route("/fashion-scenario/test-poc/", methods=['POST'])
def test_poc():
    global EXPERIMENT
    body_json = request.get_json()
    username = body_json["username"]
    exp_name = body_json["exp_name"]
    EXPERIMENT.set_experiment(username, exp_name)
    resp = jsonify({'username': username})

    return resp