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
    if EXPERIMENT.status_exp == "ready_to_setup" or EXPERIMENT.status_exp == "setup_done":
        EXPERIMENT.set_experiment(username, exp_name)
        resp = jsonify({
            'status': EXPERIMENT.status_exp, 
            'username': EXPERIMENT.username,
            'exp_name' : EXPERIMENT.exp_name            })
    else:
        resp = jsonify({'msg': 'Can not setup the experiment!'}) 
    
    return resp


#TODO: complete the API 
#manage here the status order setup_done
#Not wait the end of CL tr (rapid answer)
@base_scenario.route("/base-scenario/<username>/exec/<exp_name>", methods=['POST'])
def execute_experiment(username, exp_name):
    if request.method == 'POST':
        resp = jsonify({'status': 'CL-Training-execution'})
    
    return resp


#TODO: complete the API
#return: msg if not CL tr end or it is in different status | results and model -> execution | ready_setup
@base_scenario.route("/base-scenario/<username>/results/<exp_name>", methods=['GET'])
def get_experiment_resutls_model(username, exp_name):
    resp = jsonify({'results': {}, 'model': 'Pytorch-format'})
    
    return resp


"""
# Json like request...
{
    "username": "MarioRossi",
    "exp_name": "BaseUserExperiment",
    "config" : "others"
}
"""