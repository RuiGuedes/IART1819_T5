from src.Dataset import Dataset
from src.Model import Model

#####################
#     TEST FILE     #
#####################

# 1.0
Y1 = "I have been on this birth control for about a month and while I&#039;m aware that it&#039;s not long enough for "\
     "the pill to really set in, I&#039;ve suffered major side effects that are important to know about. "

# 4.0
Y2 = "I have been on this for about a month now. I&#039;m just so sleepy all the time. I can&#039;t snap out of it " \
     "and even on the lowest dosage (40mg at night) I can&#039;t kick it. I feel like I&#039;m a different "

# 8.0
Y3 = "I&#039;m 19 years old had a daughter who&#039;s now 6 months old, Never used a birth control and decided to go " \
     "with the Mirena I&#039;m bad at remembering things. I got the Mirena inserted last week even "

# 5.0
Y4 = "I have had Mirena for a little over a month now. As soon as I put it in I got acne, its been a problem for me " \
     "when I was in my teens and was almost completely gone by time I was 20.  I am 22 almost 23 and now it&# "

model = Model(Dataset('small.xlsx'))

model.set_clf_to_support_vector_machine('SVR')
model.train_model()
print(model.predict(Y1))
