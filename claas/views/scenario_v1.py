from flakon import JsonBlueprint
from flask import abort, jsonify, request

#TODO: import avalanche modules

scenario_v1 = JsonBlueprint('scenario_v1', __name__)

"Global Variable"
#TODO

"""
API
"""
@scenario_v1.route("/avalanche/scenario-v1/<username>", methods=['GET','POST'])
def setup_experiment(username):
    if request.method == 'POST':
        resp = json.dumps({'status': 'setup-done', 'num_exp': '3'})
    elif request.method == 'GET':
        resp = json.dumps({'model': 'modelX', 'resutls': 'res'})
    
    return resp


@scenario_v1.route("/avalanche/scenario-v1/<username>/status", methods=['POST'])
def execute_experiment(username):
    resp = json.dumps({'status': 'run experiment', 'num_exp': '3'})
    
    return resp



"""
Utility function/Class  below
"""
class Experiment:
    """
        TODO: refactoring of the comment
        Manage all the experiment setting 
    """
    def __init__(self):
        """
            TODO: refactoring of the param
            :param ...
        """
        self.dataset =  []
        self.num_experiences = None
        self.model = None #
        self.monitoring_logger = None
        self.metrics = []
        self.user_options = None
        self.username = None
        self.resutls = None #
        self.status_exp = None
    
    #TODO: write all methods

"""
# Json like request...
{
  "dataset": "MNIST",
  "num_experiences": 3,
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