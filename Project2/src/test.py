from src.Dataset import Dataset
from src.Model import *
from src.SVM import *
from src.DecisionTrees import *
from src.NeuralNetworks import *

#####################
#     TEST FILE     #
#####################

# 1.0
Y1 = "I have been on this birth control for about a month and while I&#039;m aware that it&#039;s not long enough " \
     "for the pill to really set in, I&#039;ve suffered major side effects that are important to know about. This " \
     "pill is causing me to have a second period this month, and I&#039;m anemic, so it&#039;s making me feel " \
     "extremely fatigued. It&#039;s also spiked very very severe depression and a loss of appetite. "

# 4.0
Y2 = "I have been on this for about a month now. I&#039;m just so sleepy all the time. I can&#039;t snap out of it " \
     "and even on the lowest dosage (40mg at night) I can&#039;t kick it. I feel like I&#039;m a different person, " \
     "not in a good way. I&#039;m going to call my doctor and tell her that I discontinued it on my own. I cannot " \
     "perform my daily functions as a wife and mother when I feel like I&#039;m going to fall asleep behind the wheel. "

# 8.0
Y3 = "I&#039;m 19 years old had a daughter who&#039;s now 6 months old, Never used a birth control and decided to go " \
     "with the Mirena I&#039;m bad at remembering things. I got the Mirena inserted last week even though I had a " \
     "baby it was a little painful inserting it she said my cervix was pretty high. The next day I was normal. Drink " \
     "some ibuprofen you&#039;ll be fine. I get cramps here and there but again it&#039;s only been a week my " \
     "boyfriend says he only feels the strings but it doesn&#039;t bother it only tickles, so far so good. "

# 5.0
Y4 = "I have had Mirena for a little over a month now. As soon as I put it in I got acne, its been a problem for me " \
     "when I was in my teens and was almost completely gone by time I was 20.  I am 22 almost 23 and now it&#039;s " \
     "almost as bad as when I was 15. I have to wash my face every day with acne creams, to help control the break " \
     "outs, most of which are on my back. I have all sorts of mood swings and my husband says that I haven&#039;t " \
     "really been the same since it was inserted. I am going to be looking into a way to off set this. Every once " \
     "and a while I will get the breast tenderness, but it&#039;s not much worse then when I was breastfeeding and " \
     "often goes away in minutes. I have a horrible time remembering to do things, so when I was taking a pill " \
     "everyday I " \
     "had to rely on my cellphone alarm going off to take the pill and even then if it wasn&#039;t close by or if I " \
     "was in the middle of doing something I wouldn&#039;t stop to go take the pill. I love that I don&#039;t really " \
     "have to worry about it.  My doctor told me since I hadn&#039;t been getting my period while breastfeeding, " \
     "Mirena would more then likely stop my periods, which so far I haven&#039;t even spotted one day.  I " \
     "haven&#039;t had any problems with weight gain. I have maintained the same weight as when it was inserted, " \
     "though I am trying now to start losing weight, so we shall see how that goes. Overall at this moment I would " \
     "recommend it to others. As long as I can off set this funk I am in. "

model = SVC(Dataset('small.xlsx'))

# CLF

model.train_model(model.get_algorithm())
print(model.predict(Y1))
print(model.predict(Y2))
print(model.predict(Y3))
print(model.predict(Y4))

# GRID CLF

# model.train_model(model.get_algorithm(), True)
# print(model.predict(Y1, True))
# print(model.predict(Y2, True))
# print(model.predict(Y3, True))
# print(model.predict(Y4, True))
# model.show_best_param(model.get_algorithm(), model.get_algorithm_gs_param())
