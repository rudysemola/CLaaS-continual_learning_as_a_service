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