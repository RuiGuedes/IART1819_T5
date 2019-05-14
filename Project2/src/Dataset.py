import re
import pandas as pd
from html2text import unescape
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


# ---------------------------------------------------
#   Dataset class where all information about the
#   the dataset will be stored and manipulated
# ---------------------------------------------------
class Dataset:
    filename = ''  # Name of the file to be parsed
    reviews = []   # Structure containing drug reviews
    evaluations = []   # Structure containing drug ratings
    dsdict = {'review': reviews, 'evaluation': evaluations}  # Dataset dictionary

    # ---------------------------------------------------
    #   Dataset class default constructor
    #       + Filename: File to be read
    # ---------------------------------------------------
    def __init__(self, filename):
        self.filename = filename
        self.parse_excel_file()

    # ---------------------------------------------------
    #   Function responsible for loading and store
    #   dataset information
    # ---------------------------------------------------
    def parse_excel_file(self):
        df = pd.read_excel('../dataset/parsed/' + self.filename, 'Sheet1')

        # Builds stemmer and stopwords list
        stemmer = SnowballStemmer('english')
        words = stopwords.words('english')

        # Remove html encoding from reviews
        df['review'] = df['review'].apply(unescape, unicode_snob=True)

        # Apply text stemming
        df['review'] = df['review'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]", " ", x).split() if i not in words]).lower())

        self.parse_column(df['review'], 'review')
        self.parse_column(df['evaluation'], 'evaluation')

    # ---------------------------------------------------
    #   Function responsible for parsing a column from
    #   an object array to an array
    # ---------------------------------------------------
    def parse_column(self, column, identifier):
        for item in column:
            self.dsdict[identifier].append(item)

    # ---------------------------------------------------
    #   Returns the column containing the drugs reviews
    # ---------------------------------------------------
    def get_reviews(self):
        return self.reviews

    # ---------------------------------------------------
    #   Returns the column containing the drugs ratings
    # ---------------------------------------------------
    def get_evaluations(self):
        return self.evaluations

    # ---------------------------------------------------
    #   Returns all dataset information
    # ---------------------------------------------------
    def get_info(self):
        return [self.reviews, self.evaluations]
