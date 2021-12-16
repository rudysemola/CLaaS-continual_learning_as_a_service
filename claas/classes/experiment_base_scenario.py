import avalanche
from avalanche.benchmarks.classic import SplitMNIST
from avalanche.models import SimpleMLP
from avalanche.training.plugins import EvaluationPlugin
from avalanche.logging import InteractiveLogger
from avalanche.evaluation.metrics import accuracy_metrics, \
    timing_metrics, cpu_usage_metrics, disk_usage_metrics, gpu_usage_metrics, ram_usage_metrics
from avalanche.training.strategies import Replay

from torch.optim import SGD
from torch.nn import CrossEntropyLoss



class ExperimentBaseScenario:
    """
        TODO: refactoring of the comment
        Manage all the experiment setting 
    """

    def __init__(self):
        """
            TODO: refactoring of the param
            :param ...
        """
        self.benchmark = None
        self.first_done = False #change after first TR

        self.model = None #
        self.eval_plugin = None
        self.username = ''
        self.exp_name = ''
        self.monitoring_logger = None
        self.results1 = {} #
        self.results2 = {} #
        self.status_exp = 'ready_to_setup'
    

    def set_experiment(self, username, exp_name):
        # Datasets available for current experiment
        self.benchmark = SplitMNIST(n_experiences=5, shuffle=False)

        # model
        self.model = SimpleMLP(num_classes=self.benchmark.n_classes)

        #metrics, logger and eval plugin
        self.monitoring_logger = InteractiveLogger()
        self.eval_plugin = EvaluationPlugin(
            accuracy_metrics(epoch=True, experience=True, stream=True),
            timing_metrics(epoch=True, experience=True),
            cpu_usage_metrics(experience=True),
            disk_usage_metrics(epoch=True, experience=True, stream=True),
            ram_usage_metrics(epoch=True, experience=True, stream=True),
            loggers=[self.monitoring_logger]
        ) # gpu_usage_metrics

        # setup username and exsperience name
        self.username = username
        self.exp_name = exp_name

        # change the experiment status
        self.status_exp = 'ready_to_CLtrain'


    def run_experiment(self):
        # CREATE THE STRATEGY INSTANCE (Replay)
        cl_strategy = Replay(
            self.model, SGD(self.model.parameters(), lr=0.001, momentum=0.9),
            CrossEntropyLoss(), train_mb_size=500, train_epochs=1, eval_mb_size=100,
            evaluator=self.eval_plugin)

        # TRAINING LOOP
        print('Starting experiment...')
        if self.first_done is False:
            for i, exp in enumerate(self.benchmark.train_stream):
                if i >= 3:
                    break
                cl_strategy.train(exp, num_workers=4)
                self.results1 = cl_strategy.eval(self.benchmark.test_stream[:i + 1], num_workers=4)
            self.first_done = True
            self.status_exp = 'CLtr_done'
        elif self.first_done is True:
            for i, exp in enumerate(self.benchmark.train_stream):
                if i >= 3:
                    cl_strategy.train(exp, num_workers=4)
                    self.results2 = cl_strategy.eval(self.benchmark.test_stream[:i + 1], num_workers=4)
            self.first_done = None
            self.status_exp = 'CLtr_done'
        else: #None
            self.status_exp = 'END scenario DEMO'

    
    def save_model(self, username, exp_name):
        torch.save(self.model, 'claas/store_models/'+str(username)+'_'+str(exp_name)+'_simpleModel.pt')
        model_path = 'claas/store_models/'+str(username)+'_'+str(exp_name)+'_simpleModel.pt'
        
        return model_path