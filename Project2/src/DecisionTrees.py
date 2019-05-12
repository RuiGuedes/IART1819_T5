import os
from sklearn import tree
from src.Model import Model
from joblib import dump, load


# ---------------------------------------------------
#   DecisionTreeClassifier model class
# ---------------------------------------------------
class DecisionTreeClassifier(Model):
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
            dump(self.clf, '../joblib/DecisionTreeClassifier.joblib')


# ---------------------------------------------------
#   DecisionTreeRegressor model class
# ---------------------------------------------------
class DecisionTreeRegressor(Model):
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=5, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'DecisionTreeRegressor')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/DecisionTreeRegressor.joblib'):
            self.clf = load('../joblib/DecisionTreeRegressor.joblib')
        else:
            self.clf = tree.DecisionTreeRegressor()
            dump(self.clf, '../joblib/DecisionTreeRegressor.joblib')
