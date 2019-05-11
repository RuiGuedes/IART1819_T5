import os
from sklearn import svm
from sklearn import tree
from joblib import dump, load
from src.LemmaTokenizer import LemmaTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier, MLPRegressor


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

    # ---------------------------------------------------
    #   Model class default constructor
    #       + dataset: Dataset object containing all
    #                  information
    # ---------------------------------------------------
    def __init__(self, dataset):
        self.dataset = dataset
        self.parse_dataset()

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
    #   classifier. If already created it loads it from
    #   a file otherwise creates it
    #       + algorithm: algorithm to be used for train-
    #                    -ing and prediction
    # ---------------------------------------------------
    def set_classifier(self, algorithm):
        if os.path.isfile('../joblib/' + algorithm + '.joblib'):
            self.clf = load('../joblib/' + algorithm + '.joblib')
        else:
            self.init_classifier(algorithm)
            dump(self.clf, '../joblib/' + algorithm + '.joblib')

    # ---------------------------------------------------
    #   Function responsible for initializing the model
    #   classifier.
    #       + algorithm: algorithm to be used for train-
    #                    -ing and prediction
    # ---------------------------------------------------
    def init_classifier(self, algorithm):
        if algorithm == 'SVC':
            self.clf = svm.SVC(gamma='auto')
        elif algorithm == 'LinearSVC':
            self.clf = svm.LinearSVC()
        elif algorithm == 'LinearSVR':
            self.clf = svm.LinearSVR()
        elif algorithm == 'SVR':
            self.clf = svm.SVR(gamma='auto')
        elif algorithm == 'DecisionTreeClassifier':
            self.clf = tree.DecisionTreeClassifier()
        elif algorithm == 'DecisionTreeRegressor':
            self.clf = tree.DecisionTreeRegressor()
        elif algorithm == 'MLPClassifier':
            self.clf = MLPClassifier()
        else:
            self.clf = MLPRegressor()

    # ---------------------------------------------------
    #   Function responsible for training the model
    #   classifier using the X_train and X_target varia-
    #   -bles
    # ---------------------------------------------------
    def train_model(self):
        self.clf.fit(self.X_train, self.X_target)

    # ---------------------------------------------------
    #   Function responsible for predicting a rating
    #   for a certain review
    # ---------------------------------------------------
    def predict(self, review):
        return self.clf.predict(self.vectorizer.transform([review]))
