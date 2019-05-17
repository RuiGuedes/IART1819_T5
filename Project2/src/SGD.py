import os
import numpy as np
from src.Model import Model
from joblib import load
from sklearn.linear_model import SGDClassifier


# ---------------------------------------------------
#   SVC model class
# ---------------------------------------------------
class SGD(Model):
    parameters = {}  # Grid search parameters

    # ---------------------------------------------------
    #   SGD class constructor
    #       + train_dataset: Dataset object containing
    #                       all training information
    #       + train_dataset: Dataset object containing
    #                       all training information
    # ---------------------------------------------------
    def __init__(self, train_dataset, test_dataset, grid_search=False, cv=10, iid=False, n_jobs=None):
        super().__init__(train_dataset, test_dataset, cv, iid, n_jobs, "SGD")
        self.grid_search = grid_search
        self.set_classifier()
        if self.grid_search:
            self.set_grid_search_classifier(self.parameters)

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

    # ---------------------------------------------------
    #   Function responsible for retrieving the y_score
    #   which consists on the array having all
    #   estimations
    # ---------------------------------------------------
    def get_y_score(self):
        if self.grid_search:
            return self.gs_clf.decision_function(self.vectorized_reviews)

        return self.clf.decision_function(self.vectorized_reviews)
