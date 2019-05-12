import os
from src.Model import Model
from joblib import dump, load
from sklearn.neural_network import MLPClassifier, MLPRegressor


# ---------------------------------------------------
#   NeuralNetworkClassifier model class
# ---------------------------------------------------
class NeuralNetworkClassifier(Model):
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
            dump(self.clf, '../joblib/MLPClassifier.joblib')


# ---------------------------------------------------
#   NeuralNetworkRegressor model class
# ---------------------------------------------------
class NeuralNetworkRegressor(Model):
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
            dump(self.clf, '../joblib/MLPRegressor.joblib')
