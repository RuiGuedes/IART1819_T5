import pandas as pd


# ---------------------------------------------------
#   Dataset class where all information about the
#   the dataset will be stored and manipulated
# ---------------------------------------------------
class Dataset:
    filename = ''  # Name of the file to be parsed
    drugs = []     # Structure containing drug names
    reviews = []   # Structure containing drug reviews
    ratings = []   # Structure containing drug ratings
    dsdict = {'drugName': drugs, 'review': reviews, 'rating': ratings}  # Dataset dictionary

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

        self.parse_column(df['drugName'], 'drugName')
        self.parse_column(df['review'].values.astype('U'), 'review')
        self.parse_column(df['rating'], 'rating')

    # ---------------------------------------------------
    #   Function responsible for parsing a column from
    #   an object array to an array
    # ---------------------------------------------------
    def parse_column(self, column, identifier):
        for item in column:
            self.dsdict[identifier].append(item)

    # ---------------------------------------------------
    #   Returns the column containing the drugs name
    # ---------------------------------------------------
    def get_drugs(self):
        return self.drugs

    # ---------------------------------------------------
    #   Returns the column containing the drugs reviews
    # ---------------------------------------------------
    def get_reviews(self):
        return self.reviews

    # ---------------------------------------------------
    #   Returns the column containing the drugs ratings
    # ---------------------------------------------------
    def get_ratings(self):
        return self.ratings

    # ---------------------------------------------------
    #   Returns all dataset information
    # ---------------------------------------------------
    def get_info(self):
        return [self.drugs, self.reviews, self.ratings]
