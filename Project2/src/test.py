from src.Dataset import *
from src.LemmaTokenizer import *
from sklearn.feature_extraction.text import TfidfVectorizer

#####################
#     TEST FILE     #
#####################

model = Dataset('small.xlsx')

reviews = []

for review in model.get_reviews():
    reviews.append(review)

# print(model.get_ratings())

vectorizer = TfidfVectorizer(tokenizer=LemmaTokenizer())
X = vectorizer.fit_transform(reviews)

# print(vectorizer)

# print(vectorizer.get_feature_names())

# print(X.shape)
