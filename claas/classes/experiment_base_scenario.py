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
        self.num_tot_exps = 0
        self.model = None #
        self.monitoring_logger = None
        self.metrics = []
        self.user_options = None
        self.username = ''
        self.results = {} #
        self.status_exp = None
    
    
    #TODO: write all methods needed