from src.Dataset import Dataset
from src.Model import Model
from src.SVM import SVC, LinearSVC
from src.SGD import SGD
from src.DecisionTrees import DecisionTreeClassifier
from src.NeuralNetworks import NeuralNetworkClassifier

#####################
#     TEST FILE     #
#####################

# from sklearn import metrics
train = Dataset('train_1K.xlsx')
test = Dataset('test_1K.xlsx')

model = LinearSVC(train, test, True)

# CLF
# model.train_model()
# model.predict()
# model.statistics.show_all()

# GRID CLF

model.train_model(True)
model.predict(True)
# model.show_best_param(model.get_algorithm(), model.get_algorithm_gs_param())
