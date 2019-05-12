import os
from sklearn import svm
from src.Model import Model
from joblib import dump, load


# ---------------------------------------------------
#   SVC model class
# ---------------------------------------------------
class SVC(Model):
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=10, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'SVC')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/SVC.joblib'):
            self.clf = load('../joblib/SVC.joblib')
        else:
            self.clf = svm.SVC(gamma='auto')
            dump(self.clf, '../joblib/SVC.joblib')


# ---------------------------------------------------
#   LinearSVC model class
# ---------------------------------------------------
class LinearSVC(Model):
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=5, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'LinearSVC')

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
            dump(self.clf, '../joblib/LinearSVC.joblib')


# ---------------------------------------------------
#   LinearSVR model class
# ---------------------------------------------------
class LinearSVR(Model):
    parameters = {}     # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=5, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'LinearSVR')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/LinearSVR.joblib'):
            self.clf = load('../joblib/LinearSVR.joblib')
        else:
            self.clf = svm.LinearSVR()
            dump(self.clf, '../joblib/LinearSVR.joblib')


# ---------------------------------------------------
#   SVR model class
# ---------------------------------------------------
class SVR(Model):
    parameters = {'kernel': ('linear', 'rbf')}     # Grid search parameters

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv=5, iid=False, n_jobs=None):
        super().__init__(dataset, cv, iid, n_jobs)
        self.set_classifier()
        self.set_grid_search_classifier(self.parameters, 'SVR')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_classifier(self):
        if os.path.isfile('../joblib/SVR.joblib'):
            self.clf = load('../joblib/SVR.joblib')
        else:
            self.clf = svm.SVR(gamma='auto')
            dump(self.clf, '../joblib/SVR.joblib')
