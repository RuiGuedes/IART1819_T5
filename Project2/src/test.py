from src.Dataset import Dataset
from src.Model import *
from src.SVM import *
from src.SGD import *
from src.DecisionTrees import *
from src.NeuralNetworks import *

#####################
#     TEST FILE     #
#####################

train = Dataset('train.xlsx')
test = Dataset('test.xlsx')

model = SGD(train, test)

# CLF

model.train_model()
model.predict()
model.show_statistics()

# GRID CLF

# model.train_model(model.get_algorithm(), True)
# print(model.predict(Y1, True))
# print(model.predict(Y2, True))
# print(model.predict(Y3, True))
# print(model.predict(Y4, True))
# model.show_best_param(model.get_algorithm(), model.get_algorithm_gs_param())
