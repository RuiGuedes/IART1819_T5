import os
from joblib import dump, load
from src.Statistics import Statistics
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer


# ---------------------------------------------------
#   Model class where all model information is
#   present and where all algorithms are defined
# ---------------------------------------------------
class Model:
    X_train = None          # Model input used to train
    X_target = None         # Model output used to train
    train_dataset = None    # Dataset object containing all training dataset information
    test_dataset = None     # Dataset object containing all testing dataset information
    vectorizer = None       # Model vectorizer
    algorithm = None        # Model used algorithm
    clf = None              # Model classifier
    gs_clf = None           # Model grid search classifier
    cv = 10                 # Grid search <cv> attribute
    iid = False             # Grid search <iid> attribute
    n_jobs = None           # Grid search <n_jobs> attribute
    predicted = None        # Predicted results
    statistics = None       # Model statistics

    # ---------------------------------------------------
    #   Model class constructor
    #       + train_dataset: Dataset object containing
    #                       all training information
    #       + train_dataset: Dataset object containing
    #                       all training information
    # ---------------------------------------------------
    def __init__(self, train_dataset, test_dataset, cv, iid, n_jobs, algorithm):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.parse_train_dataset()

        self.cv = cv
        self.iid = iid
        self.n_jobs = n_jobs

        self.algorithm = algorithm
        self.statistics = Statistics(self)

    # ---------------------------------------------------
    #   Function responsible for parsing the dataset
    #   in order to initialize all model class variables
    # ---------------------------------------------------
    def parse_train_dataset(self):
        self.init_vectorizer()
        self.init_input()
        self.X_target = self.train_dataset.get_evaluations()

    # ---------------------------------------------------
    #   Function responsible for initializing the model
    #   vectorizer. If already created it loads it from
    #   a file otherwise creates it
    #       + lemmatizing: Defines whether the tokenizer
    #                      should use the LemmaTokenizer
    #                      class
    # ---------------------------------------------------
    def init_vectorizer(self):
        if os.path.isfile('../joblib/vectorizer.joblib'):
            self.vectorizer = load('../joblib/vectorizer.joblib')
        else:
            self.vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english', ngram_range=(1, 2),
                                              lowercase=False)

    # ---------------------------------------------------
    #   Function responsible for initializing the model
    #   input. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def init_input(self):
        if os.path.isfile('../joblib/X_train.joblib'):
            self.X_train = load('../joblib/X_train.joblib')
        else:
            self.X_train = self.vectorizer.fit_transform(self.train_dataset.get_reviews())
            dump(self.X_train, '../joblib/X_train.joblib')
            dump(self.vectorizer, '../joblib/vectorizer.joblib')

    # ---------------------------------------------------
    #   Function responsible for setting the model
    #   grid search classifier. If already created it loads it from
    #   a file otherwise creates it
    # ---------------------------------------------------
    def set_grid_search_classifier(self, parameters):
        if os.path.isfile('../joblib/gs_' + self.algorithm + '.joblib'):
            self.gs_clf = load('../joblib/gs_' + self.algorithm + '.joblib')
        else:
            self.gs_clf = GridSearchCV(self.clf, parameters, cv=self.cv, iid=self.iid, n_jobs=self.n_jobs)
            dump(self.gs_clf, '../joblib/gs_' + self.algorithm + '.joblib')

    # ---------------------------------------------------
    #   Function responsible for training the model
    #   classifier using the X_train and X_target varia-
    #   -bles
    # ---------------------------------------------------
    def train_model(self, gs_cfl=False):
        if gs_cfl:
            self.gs_clf = self.gs_clf.fit(self.X_train, self.X_target)
        else:
            self.clf = self.clf.fit(self.X_train, self.X_target)
            dump(self.clf, '../joblib/' + self.algorithm + '.joblib')

    # ---------------------------------------------------
    #   Function responsible for predicting a rating
    #   for a certain review
    # ---------------------------------------------------
    def predict(self, gs_cfl=False):
        vectorized_reviews = self.vectorizer.transform(self.train_dataset.
                                                       parse_list_of_reviews(self.test_dataset.get_reviews()))

        if gs_cfl:
            self.predicted = self.gs_clf.predict(vectorized_reviews)
        else:
            self.predicted = self.clf.predict(vectorized_reviews)

    # ---------------------------------------------------
    #   Function responsible for showing the best
    #   parameters for a certain algorithm
    # ---------------------------------------------------
    def show_best_param(self, algorithm, parameters):
        print("Best parameters for " + algorithm + " algorithm:")
        for param_name in parameters:
            print(param_name + ": " + self.gs_clf.best_params_[param_name])
