import os
from sklearn import tree
from src.Model import Model
from joblib import load


# ---------------------------------------------------
#   DecisionTreeClassifier model class
# ---------------------------------------------------
class DecisionTreeClassifier(Model):
    algorithm = "DecisionTreeClassifier"
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=5, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'DecisionTreeClassifier')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/DecisionTreeClassifier.joblib'):
            self.clf = load('../joblib/DecisionTreeClassifier.joblib')
        else:
            self.clf = tree.DecisionTreeClassifier()

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
