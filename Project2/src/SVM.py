import os
from sklearn import svm
from src.Model import Model
from joblib import load


# ---------------------------------------------------
#   LinearSVC model class
# ---------------------------------------------------
class LinearSVC(Model):
    parameters = {'loss': ('hinge', 'squared_hinge'),
                  'tol': (1e-2, 1e-4)}  # Grid search parameters

    # ---------------------------------------------------
    #   LinearSVC class constructor
    #       + train_dataset: Dataset object containing
    #                       all training information
    #       + train_dataset: Dataset object containing
    #                       all training information
    # ---------------------------------------------------
    def __init__(self, train_dataset, test_dataset, grid_search=False, cv=5, iid=False, n_jobs=None):
        super().__init__(train_dataset, test_dataset, cv, iid, n_jobs, "LinearSVC")
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
        if os.path.isfile('../joblib/LinearSVC' + '_' + self.train_dataset.get_dataset_size() + '.joblib'):
            self.clf = load('../joblib/LinearSVC' + '_' + self.train_dataset.get_dataset_size() + '.joblib')
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
        if self.grid_search:
            return self.gs_clf.decision_function(self.vectorized_reviews)

        return self.clf.decision_function(self.vectorized_reviews)
