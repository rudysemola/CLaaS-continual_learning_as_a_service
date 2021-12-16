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
        self.benchmark = None
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
        self.status_exp = 'setup_done'


    #TODO: run the experiment
    def run_experiment(self):
        # CREATE THE STRATEGY INSTANCE (Replay)
        cl_strategy = Replay(
            model, SGD(model.parameters(), lr=0.001, momentum=0.9),
            CrossEntropyLoss(), train_mb_size=500, train_epochs=1, eval_mb_size=100,
            evaluator=self.eval_plugin)

        # TRAINING LOOP
        print('Starting experiment...')
        #if self.first_done is False:

        #return #TODO 


    #TODO: retrive the results of experiment and model like pytorch format
    def get_resutls_model(self):
        pass