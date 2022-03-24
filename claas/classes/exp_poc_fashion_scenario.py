"Avalanche import"
import avalanche
from avalanche.benchmarks.generators import nc_benchmark
from avalanche.logging import InteractiveLogger
from avalanche.training.plugins import EvaluationPlugin
from avalanche.training.strategies import Cumulative, Replay, JointTraining

"Pytorch import"
import torch
from torch.optim import SGD
from torch.nn import CrossEntropyLoss

"PoC file"
from ..poc_fashion.deep_fashion_cate_attr import DeepFashion
from ..poc_fashion.utils_config import DatasetSetting, Timer
from ..poc_fashion.global_cate_fashion_predictor import GlobalCatePredictorFashion
from ..poc_fashion.topk_acc import *


#TODO
class ExperimentFashionScenario:
    """
        Manage all the experiment setting for PoC (Fashion Domain DEMO)
    """

    def __init__(self):
        """
            :param ...
        """


    def set_experiment(self, username, exp_name):
        pass

    def run_experiment(self):
        pass

    def save_model(self, username, exp_name):
        pass
