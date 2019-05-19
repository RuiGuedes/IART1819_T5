import PySimpleGUI as sg
import matplotlib.pyplot as plt
from src.Dataset import Dataset
from src.SVM import LinearSVC
from src.SGD import SGD
from src.KNeighbors import KNeighbors
from src.DecisionTrees import DecisionTreeClassifier
from src.NeuralNetworks import NeuralNetworkClassifier
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import tkinter as Tk
import matplotlib

matplotlib.use('TkAgg')


class GUI:
    train_dataset = None    # Train dataset
    test_dataset = None  # Test dataset
    gs_clf = None   # Grid search classifier: True if active false otherwise
    model = None    # Model selected to be used
    window = None   # Displayed GUI window
    lock = False    # Lock initialize options
    best_param_state = True     # Is grid search: True or False
    dataset_size_dict = {100: '100.xlsx', 1000: '1K.xlsx', 10000: '10K.xlsx'}   # Dataset dictionary
    algorithm_dict = {1: 'SGD', 2: 'KNeighbors', 3: 'LinearSVC',
                      4: 'DecisionTreeClassifier', 5: 'NeuralNetworkClassifier'}    # Dataset dictionary
    statistics_dict = {1: 'Classification Report', 2: 'Accuracy Score', 3: 'Best Parameters', 4: 'Confusion Matrix',
                       5: 'Learning Curve', 6: 'ROC Curve', 7: 'Precision Recall Curve'}    # Statistics dictionary

    # ---------------------------------------------------
    #   Function responsible for initializing the GUI
    #   and to perform each available action
    # ---------------------------------------------------
    def start(self):
        if self.window is not None:
            self.window.Close()

        layout = [
            [sg.Text('Drug Analysis', size=(30, 1), justification='center', font=("Courier", 30),
                     relief=sg.RELIEF_RIDGE)],
            [sg.Frame(layout=[
                [sg.Radio('100 samples', "DATASET"),
                 sg.Radio('1K samples', "DATASET", default=True),
                 sg.Radio('10K samples', "DATASET")]],
                title='Dataset Size', title_color='Blue', relief=sg.RELIEF_SUNKEN)],
            [sg.Frame(layout=[
                [sg.Radio('SGD', "ALGORITHM"),
                 sg.Radio('KNeighbors Classifier', "ALGORITHM"),
                 sg.Radio('LinearSVC', "ALGORITHM", default=True),
                 sg.Radio('Decision Tree Classifier', "ALGORITHM"),
                 sg.Radio('Neural Network Classifier', "ALGORITHM")],
                [sg.Checkbox('Use Grid-Search Classifier', key='Grid-Search', enable_events=True)]],
                title='Algorithm', title_color='Black', relief=sg.RELIEF_SUNKEN)],
            [sg.Frame(layout=[
                [sg.Button('Initialize', button_color=('white', 'green'), disabled=False, key='Initialize'),
                 sg.Button('Train', button_color=('white', 'grey'), disabled=True, key='Train'),
                 sg.Button('Predict', button_color=('white', 'grey'), disabled=True, key='Predict')]],
                title='Model', title_color='Blue', relief=sg.RELIEF_SUNKEN)],
            [sg.Frame(layout=[
                [sg.Checkbox('Classification Report')],
                [sg.Checkbox('Accuracy Score')],
                [sg.Checkbox('Best Parameters', key='Best-Param', disabled=self.best_param_state)],
                [sg.Checkbox('Confusion Matrix')],
                [sg.Checkbox('Learning Curve')],
                [sg.Checkbox('ROC Curve')],
                [sg.Checkbox('Precision Recall Curve')],
                [sg.Button('Display', button_color=('white', 'grey'), disabled=True, key='Display')]],
                title='Statistics', key='Statistics', title_color='Blue', relief=sg.RELIEF_SUNKEN)],
            [sg.Frame(layout=[
                [sg.Text('', key='TextContent')]],
                title='', key='Text', visible=False, title_color='Blue', relief=sg.RELIEF_SUNKEN)]
        ]

        self.window = sg.Window('Machine Learning - GUI', default_element_size=(50, 5), grab_anywhere=False). \
            Layout(layout)

        while True:
            event, values = self.window.Read()
            if event in (None, 'Exit'):
                break
            if event == 'Initialize':
                self.lock = True
                self.parse_dataset_size(list(values.values())[:3])
                self.gs_clf = list(values.values())[8]
                self.parse_algorithm(list(values.values())[3:8])

                self.window.Element('Initialize').Update(disabled=True, button_color=('white', 'grey'))
                self.window.Element('Train').Update(disabled=False, button_color=('white', 'green'))

                self.window.Refresh()
            elif event == 'Train':
                self.model.train_model()

                self.window.Element('Train').Update(disabled=True, button_color=('white', 'grey'))
                self.window.Element('Predict').Update(disabled=False, button_color=('white', 'green'))

                self.window.Refresh()
            elif event == 'Predict':
                self.model.predict()

                self.window.Element('Predict').Update(disabled=True, button_color=('white', 'grey'))
                self.window.Element('Display').Update(disabled=False, button_color=('white', 'green'))

                self.window.Refresh()
            elif event == 'Grid-Search':
                if not self.lock:
                    if self.best_param_state:
                        self.best_param_state = False
                    else:
                        self.best_param_state = True

                    self.window.Element('Best-Param').Update(disabled=self.best_param_state)
            elif event == 'Display':
                self.parse_statistics(list(values.values())[9:])

    # ---------------------------------------------------
    #   Function responsible for parsing the input
    #   relative to the dataset size selected
    # ---------------------------------------------------
    def parse_dataset_size(self, info):
        index = 100
        for item in info:
            if item:
                break
            else:
                index = index * 10

        self.train_dataset = Dataset('train_' + self.dataset_size_dict[index])
        self.test_dataset = Dataset('test_1K.xlsx')

    # ---------------------------------------------------
    #   Function responsible for parsing the input
    #   relative to the input selected
    # ---------------------------------------------------
    def parse_algorithm(self, info):
        index = 1
        for item in info:
            if item:
                algorithm = self.algorithm_dict[index]

                if algorithm == 'SGD':
                    self.model = SGD(self.train_dataset, self.test_dataset, self.gs_clf)
                elif algorithm == 'KNeighbors':
                    self.model = KNeighbors(self.train_dataset, self.test_dataset, self.gs_clf)
                elif algorithm == 'LinearSVC':
                    self.model = LinearSVC(self.train_dataset, self.test_dataset, self.gs_clf)
                elif algorithm == 'DecisionTreeClassifier':
                    self.model = DecisionTreeClassifier(self.train_dataset, self.test_dataset, self.gs_clf)
                elif algorithm == 'NeuralNetworkClassifier':
                    self.model = NeuralNetworkClassifier(self.train_dataset, self.test_dataset, self.gs_clf)
            else:
                index = index + 1

    # ---------------------------------------------------
    #   Function responsible for parsing the input
    #   relative to the statistics selected
    # ---------------------------------------------------
    def parse_statistics(self, info):
        index = 1
        for item in info:
            if item:
                fig = None
                algorithm = self.statistics_dict[index]

                if algorithm == 'Classification Report':
                    self.display_new_window(algorithm, self.model.statistics.show_classification_report())
                elif algorithm == 'Accuracy Score':
                    self.display_new_window(algorithm, self.model.statistics.show_accuracy_score())
                elif algorithm == 'Best Parameters':
                    self.display_new_window(algorithm, self.model.show_best_param(self.model.parameters))
                elif algorithm == 'Confusion Matrix':
                    fig = self.model.statistics.show_confusion_matrix()
                elif algorithm == 'Learning Curve':
                    fig = self.model.statistics.show_learning_curve()
                elif algorithm == 'ROC Curve':
                    fig = self.model.statistics.show_roc_curve()
                elif algorithm == 'Precision Recall Curve':
                    fig = self.model.statistics.show_precision_recall_curve()

                if fig is not None:
                    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

                    layout = [[sg.Canvas(size=(figure_w, figure_h), key='canvas')]]

                    window = sg.Window('Statistics', force_toplevel=True).Layout(
                        layout).Finalize()

                    _ = self.draw_figure(window.FindElement('canvas').TKCanvas, fig)

                    _, _ = window.Read()
                    plt.close()

                index = index + 1
            else:
                index = index + 1

    # ---------------------------------------------------
    #   Function responsible for drawing statistics
    # ---------------------------------------------------
    @staticmethod
    def draw_figure(canvas, figure, loc=(0, 0)):
        figure_canvas_agg = FigureCanvasAgg(figure)
        figure_canvas_agg.draw()
        figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
        figure_w, figure_h = int(figure_w), int(figure_h)
        photo = Tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
        canvas.create_image(loc[0] + figure_w / 2, loc[1] + figure_h / 2, image=photo)
        tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
        return photo

    # ---------------------------------------------------
    #   Function responsible for displaying a new
    #   window for classification report and the accuracy
    #   score
    # ---------------------------------------------------
    @staticmethod
    def display_new_window(title, content):
        layout = [
            [sg.Text('Statistics', size=(30, 1), justification='center', font=("Courier", 30),
                     relief=sg.RELIEF_RIDGE)],
            [sg.Frame(layout=[
                [sg.Text(content, key='TextContent')]],
                title=title, key='Text', title_color='Blue', relief=sg.RELIEF_SUNKEN)]
        ]

        statistics_window = sg.Window('Statistics', default_element_size=(50, 5), grab_anywhere=False). \
            Layout(layout)

        _, _ = statistics_window.Read()


GUI().start()
