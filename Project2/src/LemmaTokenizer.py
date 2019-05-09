from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer


# ---------------------------------------------------
#   Lemma tokenizer class used to add fancy token-
#   -level analysis such as lemmatizing that is not
#   included in the scikit-learn codebase
# ---------------------------------------------------
class LemmaTokenizer(object):

    # ---------------------------------------------------
    #   Lemma tokenizer default constructor
    # ---------------------------------------------------
    def __init__(self):
        self.wnl = WordNetLemmatizer()

    # ---------------------------------------------------
    #   Lemmatize review passed as parameter
    #       + review: Review to be lemmatized
    # ---------------------------------------------------
    def __call__(self, review):
        return [self.wnl.lemmatize(t) for t in word_tokenize(review)]
