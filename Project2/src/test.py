from src.Dataset import Dataset
from src.Model import Model
from src.SVM import SVC, LinearSVC
from src.SGD import SGD
from src.DecisionTrees import DecisionTreeClassifier
from src.NeuralNetworks import NeuralNetworkClassifier

#####################
#     TEST FILE     #
#####################

from sklearn import metrics
train = Dataset('train.xlsx')
test = Dataset('test.xlsx')

model = SGD(train, test)

# CLF
model.train_model()
model.predict()
model.statistics.show_all()

# GRID CLF

# model.train_model(model.get_algorithm(), True)
# print(model.predict(Y1, True))
# print(model.predict(Y2, True))
# print(model.predict(Y3, True))
# print(model.predict(Y4, True))
# model.show_best_param(model.get_algorithm(), model.get_algorithm_gs_param())
