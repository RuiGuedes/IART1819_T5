import os
from sklearn import svm
from src.Model import Model
from joblib import load


# ---------------------------------------------------
#   SVC model class
# ---------------------------------------------------
class SVC(Model):
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   SVC class constructor
    #       + train_dataset: Dataset object containing
    #                       all training information
    #       + train_dataset: Dataset object containing
    #                       all training information
    # ---------------------------------------------------
    def __init__(self, train_dataset, test_dataset, cv=10, iid=False, n_jobs=None, grid_search=False):
        super().__init__(train_dataset, test_dataset, cv, iid, n_jobs, "SVC")
        self.set_classifier()
        if grid_search:
            self.set_grid_search_classifier(self.parameters)

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/SVC.joblib'):
            self.clf = load('../joblib/SVC.joblib')
        else:
            self.clf = svm.SVC(gamma=0.0001)

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
        return self.clf.decision_function(self.vectorized_reviews)


# ---------------------------------------------------
#   LinearSVC model class
# ---------------------------------------------------
class LinearSVC(Model):
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   LinearSVC class constructor
    #       + train_dataset: Dataset object containing
    #                       all training information
    #       + train_dataset: Dataset object containing
    #                       all training information
    # ---------------------------------------------------
    def __init__(self, train_dataset, test_dataset, cv=5, iid=False, n_jobs=None, grid_search=False):
        super().__init__(train_dataset, test_dataset, cv, iid, n_jobs, "LinearSVC")
        self.set_classifier()
        if grid_search:
            self.set_grid_search_classifier(self.parameters)

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/LinearSVC.joblib'):
            self.clf = load('../joblib/LinearSVC.joblib')
        else:
            self.clf = svm.LinearSVC()

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
        return self.clf.decision_function(self.vectorized_reviews)
