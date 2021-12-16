import avalanche
from avalanche.benchmarks.classic import SplitMNIST
from avalanche.models import SimpleMLP
from avalanche.training.plugins import EvaluationPlugin
from avalanche.logging import InteractiveLogger
from avalanche.evaluation.metrics import accuracy_metrics, \
    timing_metrics, cpu_usage_metrics, disk_usage_metrics, gpu_usage_metrics, ram_usage_metrics



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
        self.datasets_first_exp =  []
        self.datasets_second_exp =  []
        self.first_done = False #change after first TR

        self.model = None #
        self.eval_plugin = None
        self.username = ''
        self.exp_name = ''
        self.monitoring_logger = None
        self.results = {} #
        self.status_exp = 'ready_to_setup'
    

    def set_experiment(self, username, exp_name):
        # Datasets available for current experiment
        scenario = SplitMNIST(n_experiences=5, shuffle=False)
        i = 0
        for experience in scenario.train_stream:
            if i <3:
                self.datasets_first_exp.append(experience)
                i += 1
            else:
                self.datasets_second_exp.append(experience)
                i += 1
        print(len(self.datasets_first_exp))
        print(len(self.datasets_second_exp))
        print(i)
        # model
        self.model = SimpleMLP(num_classes=scenario.n_classes)

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
        self.status_exp = 'setup_done'


    #TODO: run the experiment
    def run_experiment(self):
        pass


    #TODO: retrive the results of experiment and model like pytorch format
    def get_resutls_model(self):
        pass