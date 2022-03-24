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

@fashion_scenario.route("/fashion-scenario/setup/", methods=['POST'])
def setup_experiment():
    global EXPERIMENT
    body_json = request.get_json()
    username = body_json["username"]
    exp_name = body_json["exp_name"]
    if EXPERIMENT.status_exp == "ready_to_setup" or EXPERIMENT.status_exp == "ready_to_CLtrain":
        EXPERIMENT.set_experiment(username, exp_name)
        resp = jsonify({})
    else:
        resp = jsonify({})

    return resp