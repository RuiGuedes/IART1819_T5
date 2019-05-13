import os
from joblib import dump, load
from src.LemmaTokenizer import LemmaTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV


# ---------------------------------------------------
#   Model class where all model information is
#   present and where all algorithms are defined
# ---------------------------------------------------
class Model:
    X_train = None      # Model input used to train
    X_target = None     # Model output used to train
    dataset = None      # Dataset object containing all dataset information
    vectorizer = None   # Model vectorizer
    clf = None          # Model classifier
    gs_clf = None       # Model grid search classifier
    cv = 10             # Grid search <cv> attribute
    iid = False         # Grid search <iid> attribute
    n_jobs = None       # Grid search <n_jobs> attribute

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset, cv, iid, n_jobs):
        self.dataset = dataset
        self.parse_dataset()

        self.cv = cv
        self.iid = iid
        self.n_jobs = n_jobs

    # ---------------------------------------------------
    #   Function responsible for parsing the dataset
    #   in order to initialize all model class variables
    # ---------------------------------------------------
    def parse_dataset(self):
        self.init_vectorizer()
        self.init_input()
        self.X_target = self.dataset.get_ratings()

    # ---------------------------------------------------
    #   Function responsible for initializing the model
    #   vectorizer. If already created it loads it from
    #   a file otherwise creates it
    #       + lemmatizing: Defines whether the tokenizer
    #                      should use the LemmaTokenizer
    #                      class
    # ---------------------------------------------------
    def init_vectorizer(self, lemmatizing=False):
        if os.path.isfile('../joblib/vectorizer.joblib'):
            self.vectorizer = load('../joblib/vectorizer.joblib')
        else:
            if lemmatizing:
                self.vectorizer = TfidfVectorizer(tokenizer=LemmaTokenizer())
            else:
                self.vectorizer = TfidfVectorizer()

    # ---------------------------------------------------
    #   Function responsible for initializing the model
    #   input. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def init_input(self):
        if os.path.isfile('../joblib/X_train.joblib'):
            self.X_train = load('../joblib/X_train.joblib')
        else:
            self.X_train = self.vectorizer.fit_transform(self.dataset.get_reviews())
            dump(self.X_train, '../joblib/X_train.joblib')
            dump(self.vectorizer, '../joblib/vectorizer.joblib')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   grid search classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_grid_search_classifier(self, parameters, algorithm):
        if os.path.isfile('../joblib/gs_' + algorithm + '.joblib'):
            self.gs_clf = load('../joblib/gs_' + algorithm + '.joblib')
        else:
            self.gs_clf = GridSearchCV(self.clf, parameters, cv=self.cv, iid=self.iid, n_jobs=self.n_jobs)
            dump(self.gs_clf, '../joblib/gs_' + algorithm + '.joblib')

    # ---------------------------------------------------
    #   Function responsible for training the model
    #   classifier using the X_train and X_target varia-
    #   -bles
    # ---------------------------------------------------
    def train_model(self, algorithm, gs_cfl=False):
        if gs_cfl:
            self.gs_clf = self.gs_clf.fit(self.X_train, self.X_target)
        else:
            self.clf = self.clf.fit(self.X_train, self.X_target)
            dump(self.clf, '../joblib/' + algorithm + '.joblib')

    # ---------------------------------------------------
    #   Function responsible for predicting a rating
    #   for a certain review
    # ---------------------------------------------------
    def predict(self, review, gs_cfl=False):
        if gs_cfl:
            return self.gs_clf.predict(self.vectorizer.transform([review]))
        else:
            return self.clf.predict(self.vectorizer.transform([review]))

    # ---------------------------------------------------
    #   Function responsible for showing the best
    #   parameters for a certain algorithm
    # ---------------------------------------------------
    def show_best_param(self, algorithm, parameters):
        print("Best parameters for " + algorithm + " algorithm:")
        for param_name in parameters:
            print(param_name + ": " + self.gs_clf.best_params_[param_name])
