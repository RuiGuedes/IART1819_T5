import os
import numpy as np
from src.Model import Model
from joblib import load
from sklearn.linear_model import SGDClassifier


# ---------------------------------------------------
#   SVC model class
# ---------------------------------------------------
class SGD(Model):
    algorithm = "SGD"
    parameters = {}  # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=10, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'SGD')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/SGD.joblib'):
            self.clf = load('../joblib/SGD.joblib')
        else:
            self.clf = SGDClassifier(loss='hinge', penalty='l2',
                                     alpha=1e-3, random_state=42,
                                     max_iter=5, tol=-np.inf)

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
