import pandas as pd


# ---------------------------------------------------
#   Dataset class where all information about the
#   the dataset will be stored and manipulated
# ---------------------------------------------------
class Dataset:
    filename = ''
    drugs = []
    reviews = []
    ratings = []

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

        self.drugs = df['drugName']
        self.reviews = df['review']
        self.ratings = df['rating']

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
