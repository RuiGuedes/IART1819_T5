import os
from src.Model import Model
from joblib import load
from sklearn.neural_network import MLPClassifier


# ---------------------------------------------------
#   NeuralNetworkClassifier model class
# ---------------------------------------------------
class NeuralNetworkClassifier(Model):
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   NeuralNetworkClassifier class constructor
    #       + train_dataset: Dataset object containing
    #                       all training information
    #       + train_dataset: Dataset object containing
    #                       all training information
    # ---------------------------------------------------
    def __init__(self, train_dataset, test_dataset, grid_search=False, cv=5, iid=False, n_jobs=None):
        super().__init__(train_dataset, test_dataset, cv, iid, n_jobs, "NeuralNetworkClassifier")
        self.set_classifier()
        if grid_search:
            self.set_grid_search_classifier(self.parameters)

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
    #   Function responsible for retrieving the y_score
    #   which consists on the array having all
    #   estimations
    # ---------------------------------------------------
    def get_y_score(self):
        return self.clf.predict_proba(self.vectorized_reviews)[:, 1]
