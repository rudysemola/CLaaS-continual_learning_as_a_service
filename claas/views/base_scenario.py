from flakon import JsonBlueprint
from flask import abort, jsonify, request

from claas.classes.experiment_base_scenario import ExperimentBaseScenario

base_scenario = JsonBlueprint('base_scenario', __name__)

"""
GLOBAL VAR
"""
EXPERIMENT = ExperimentBaseScenario()


"""
API - CLaaS (Base Scenario)
"""
@base_scenario.route("/base-scenario/setup/", methods=['POST'])
def setup_experiment():
    global EXPERIMENT
    body_json = request.get_json()
    username = body_json["username"]
    exp_name = body_json["exp_name"]
    if EXPERIMENT.status_exp == "ready_to_setup" or EXPERIMENT.status_exp == "ready_to_CLtrain":
        EXPERIMENT.set_experiment(username, exp_name)
        resp = jsonify({
            'status': EXPERIMENT.status_exp, 
            'username': EXPERIMENT.username,
            'exp_name' : EXPERIMENT.exp_name            })
    else:
        resp = jsonify({'msg': 'Can not setup the experiment! See The Status of the exsperiment', 'status': EXPERIMENT.status_exp}) 
    
    return resp


@base_scenario.route("/base-scenario/<username>/exec/<exp_name>", methods=['POST'])
def execute_experiment(username, exp_name):
    global EXPERIMENT
    if EXPERIMENT.status_exp == "ready_to_CLtrain" or EXPERIMENT.status_exp == "CLtr_done":
        EXPERIMENT.run_experiment()
        resp = jsonify({'status': EXPERIMENT.status_exp})
    else:
        resp = jsonify({'msg': 'Can not run the experiment! See The Status of the exsperiment', 'status': EXPERIMENT.status_exp}) 
    
    return resp


@base_scenario.route("/base-scenario/<username>/results/<exp_name>", methods=['GET'])
def get_experiment_resutls_model(username, exp_name):
    global EXPERIMENT
    if EXPERIMENT.status_exp == "CLtr_done":
        resp = jsonify({'model': EXPERIMENT.model.state_dict(), 'results': EXPERIMENT.results,'status': EXPERIMENT.status_exp})
    else:
        resp = jsonify({'msg': 'Can not retieve the results and model! See The Status of the exsperiment', 'status': EXPERIMENT.status_exp}) 
    
    return resp


"""
# Json like request
{
    "username": "MarioRossi",
    "exp_name": "BaseUserExperiment",
    "config" : "others"
}
"""