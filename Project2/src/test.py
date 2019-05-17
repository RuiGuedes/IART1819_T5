from src.Dataset import Dataset
from src.Model import Model
from src.SVM import LinearSVC
from src.SGD import SGD
from src.DecisionTrees import DecisionTreeClassifier
from src.NeuralNetworks import NeuralNetworkClassifier

#####################
#     TEST FILE     #
#####################

# from sklearn import metrics
train = Dataset('train_100.xlsx')
test = Dataset('test_1K.xlsx')

model = DecisionTreeClassifier(train, test)

model.train_model()
model.predict()

# CLF
# model.train_model()
# model.predict()
model.statistics.show_all()


# GRID CLF

# model.show_best_param(model.get_algorithm(), model.get_algorithm_gs_param())
