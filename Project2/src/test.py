from src.Dataset import Dataset
from src.Model import Model
from src.SVM import SVC, LinearSVC
from src.SGD import SGD
from src.DecisionTrees import DecisionTreeClassifier
from src.NeuralNetworks import NeuralNetworkClassifier

#####################
#     TEST FILE     #
#####################
import matplotlib.pyplot as plt

train = Dataset('train.xlsx')
test = Dataset('test.xlsx')

model = LinearSVC(train, test)

# CLF

model.train_model()
model.predict()
# model.get_statistics().show_statistics()
model.statistics.show_learning_curve()

plt.show()

# GRID CLF

# model.train_model(model.get_algorithm(), True)
# print(model.predict(Y1, True))
# print(model.predict(Y2, True))
# print(model.predict(Y3, True))
# print(model.predict(Y4, True))
# model.show_best_param(model.get_algorithm(), model.get_algorithm_gs_param())
