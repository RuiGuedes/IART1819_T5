import os
from src.Model import Model
from joblib import load
from sklearn.neural_network import MLPClassifier, MLPRegressor


# ---------------------------------------------------
#   NeuralNetworkClassifier model class
# ---------------------------------------------------
class NeuralNetworkClassifier(Model):
    algorithm = "NeuralNetworkClassifier"
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=5, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'NeuralNetworkClassifier')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/MLPClassifier.joblib'):
            self.clf = load('../joblib/MLPClassifier.joblib')
        else:
            self.clf = MLPClassifier()

    # ---------------------------------------------------
    #   Function responsible for retrieving the
    #   algorithm name
    # ---------------------------------------------------
    def get_algorithm(self):
        return self.algorithm

    # ---------------------------------------------------
    #   Function responsible for retrieving the grid
    #   search parameters
    # ---------------------------------------------------
    def get_algorithm_gs_param(self):
        return self.parameters


# ---------------------------------------------------
#   NeuralNetworkRegressor model class
# ---------------------------------------------------
class NeuralNetworkRegressor(Model):
    algorithm = "NeuralNetworkRegressor"
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=5, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'NeuralNetworkRegressor')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/MLPRegressor.joblib'):
            self.clf = load('../joblib/MLPRegressor.joblib')
        else:
            self.clf = MLPRegressor()

    # ---------------------------------------------------
    #   Function responsible for retrieving the
    #   algorithm name
    # ---------------------------------------------------
    def get_algorithm(self):
        return self.algorithm

    # ---------------------------------------------------
    #   Function responsible for retrieving the grid
    #   search parameters
    # ---------------------------------------------------
    def get_algorithm_gs_param(self):
        return self.parameters
