import os
from sklearn import svm
from sklearn import tree
from joblib import dump, load
from src.LemmaTokenizer import LemmaTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier, MLPRegressor


class Model:
    X_train = None
    X_target = None
    dataset = None
    vectorizer = None
    clf = None

    def __init__(self, dataset):
        self.dataset = dataset
        self.parse_dataset()

    def parse_dataset(self):
        self.init_vectorizer()
        self.init_input()
        self.X_target = self.dataset.get_ratings()

    def init_vectorizer(self, lemmatizing=False):
        if os.path.isfile('../joblib/vectorizer.joblib'):
            self.vectorizer = load('../joblib/vectorizer.joblib')
        else:
            if lemmatizing:
                self.vectorizer = TfidfVectorizer(tokenizer=LemmaTokenizer())
            else:
                self.vectorizer = TfidfVectorizer()

    def init_input(self):
        if os.path.isfile('../joblib/X_train.joblib'):
            self.X_train = load('../joblib/X_train.joblib')
        else:
            self.X_train = self.vectorizer.fit_transform(self.dataset.get_reviews())
            dump(self.X_train, '../joblib/X_train.joblib')
            dump(self.vectorizer, '../joblib/vectorizer.joblib')

    def set_clf_to_support_vector_machine(self, algorithm):
        if algorithm == 'SVC':
            self.clf = svm.SVC(gamma='auto')
        elif algorithm == 'LinearSVR':
            self.clf = svm.LinearSVR()
        elif algorithm == 'LinearSVC':
            self.clf = svm.LinearSVC()
        else:
            self.clf = svm.SVR(gamma='auto')

    def set_clf_to_decision_tree(self, algorithm):
        if algorithm == 'DecisionTreeClassifier':
            self.clf = tree.DecisionTreeClassifier()
        else:
            self.clf = tree.DecisionTreeRegressor()

    def set_clf_to_neural_network(self, algorithm):
        if algorithm == 'MLPClassifier':
            self.clf = MLPClassifier()
        else:
            self.clf = MLPRegressor

    def train_model(self):
        self.clf.fit(self.X_train, self.X_target)

    def predict(self, review):
        return self.clf.predict(self.vectorizer.transform([review]))
