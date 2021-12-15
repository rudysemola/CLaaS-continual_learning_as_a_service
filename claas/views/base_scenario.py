from flakon import JsonBlueprint
from flask import abort, jsonify, request

from class.classes.experiment_base_scenario import ExperimentBaseScenario

#TODO: import avalanche modules

base_scenario = JsonBlueprint('base_scenario', __name__)


"""
API - CLaaS (Base Scenario)
"""
#TODO: complete the API
@base_scenario.route("/base-scenario/<username>/setup", methods=['POST'])
def setup_experiment(username):
    if request.method == 'POST':
        resp = jsonify({'status': 'setup-done', 'num_tot_exps': '3'})
    
    return resp


#TODO: complete the API
@base_scenario.route("/base-scenario/<username>/exec", methods=['POST'])
def setup_experiment(username):
    if request.method == 'POST':
        resp = jsonify({'status': 'CL-Training-execution'})
    
    return resp


#TODO: complete the API
@base_scenario.route("/base-scenario/<username>/results", methods=['GET'])
def execute_experiment(username, status):
    resp = jsonify({'results': {}, 'model': 'Pytorch-format'})
    
    return resp



"""
Utility function/Class  below
"""
#TODO: if needed

"""
# Json like request...
{
  "dataset": "MNIST",
  "scenario": "SplitMNIST",
  "num_tot_exps": 3,
  "model": "replay",
  "monitoring_logger": "interactive",
  "metrics": [
    "accuracy_metrics", 
    "cpu_usage", 
    "disk_usage",
    "gpu_usage",
    "ram_usage",
    "timing"],
    "user-options": "P",
    "username": "Mario Rossi"
}
"""