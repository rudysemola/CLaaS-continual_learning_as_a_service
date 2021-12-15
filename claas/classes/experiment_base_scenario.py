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
        self.dataset =  []
        self.num_tot_exps = 0 #0->3 | 4 | 5
        self.model = None #
        self.monitoring_logger = None
        self.metrics = []
        self.user_options = None
        self.username = ''
        self.results = {} #
        self.status_exp = None
    

    #TODO: set the class param 
    def set_experiment(self):
        pass


    #TODO: run the experiment
    def run_experiment(self):
        pass


    #TODO: retrive the results of experiment and model like pytorch format
    def get_resutls_model(self):
        pass