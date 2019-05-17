import numpy as np
import matplotlib.pyplot as plt
from inspect import signature
from sklearn.model_selection import learning_curve
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_curve, auc
from sklearn.metrics import precision_recall_curve


# ---------------------------------------------------
#   Statistics class where all model statistics
#   are defined
# ---------------------------------------------------
class Statistics:
    model = None    # Associated model

    # ---------------------------------------------------
    #   Statistics class constructor
    #       + model: Model to be analysed
    # ---------------------------------------------------
    def __init__(self, model):
        self.model = model

    # ---------------------------------------------------
    #   Function responsible for displaying all the model
    #   associated statistics
    # ---------------------------------------------------
    def show_all(self):
        self.show_classification_report(True)
        self.show_accuracy_score(True)
        self.show_learning_curve(True)
        self.show_confusion_matrix(True)
        self.show_roc_curve(True)
        self.show_precision_recall_curve(True)

    # ---------------------------------------------------
    #   Function responsible for displaying the model
    #   classification report including precision, recall,
    #   f1-score and support
    # ---------------------------------------------------
    def show_classification_report(self, show=False):
        if show:
            print('Classification report: \n')
            print(classification_report(self.model.predicted, self.model.test_dataset.get_evaluations()))
        else:
            return classification_report(self.model.predicted, self.model.test_dataset.get_evaluations())

    # ---------------------------------------------------
    #   Function responsible for displaying the accuracy
    #   score
    # ---------------------------------------------------
    def show_accuracy_score(self, show=False):
        if show:
            print('Accuracy score: ' + str(accuracy_score(self.model.predicted,
                                                          self.model.test_dataset.get_evaluations())))
        else:
            return str(accuracy_score(self.model.predicted, self.model.test_dataset.get_evaluations()))

    # ---------------------------------------------------
    #   Function responsible for displaying the confusion
    #   matrix
    #       + normalize: Normalized matrix (default = true)
    # ---------------------------------------------------
    def show_confusion_matrix(self, show=False, normalize=True):
        self.plot_confusion_matrix(self.model.test_dataset.get_evaluations(), self.model.predicted,
                                   classes=['Negative', 'Positive'],
                                   normalize=normalize)
        if show:
            plt.show()
        else:
            return plt.gcf()

    # ---------------------------------------------------
    #   Function responsible for preparing the confusion
    #   matrix to be plotted
    # ---------------------------------------------------
    def plot_confusion_matrix(self, y_test, y_pred, classes,
                              normalize=False,
                              title=None,
                              cmap=plt.cm.Blues):

        np.set_printoptions(precision=2)

        if not title:
            if normalize:
                title = 'Normalized confusion matrix (' + self.model.algorithm + ')'
            else:
                title = 'Confusion matrix, without normalization (' + self.model.algorithm + ')'

        # Compute confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        # Only use the labels that appear in the data
        # classes = classes[unique_labels(y_true, y_pred)]
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        fig, ax = plt.subplots()
        im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
        ax.figure.colorbar(im, ax=ax)
        # We want to show all ticks...
        ax.set(xticks=np.arange(cm.shape[1]),
               yticks=np.arange(cm.shape[0]),
               # ... and label them with the respective list entries
               xticklabels=classes, yticklabels=classes,
               title=title,
               ylabel='True label',
               xlabel='Predicted label')

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], fmt),
                        ha="center", va="center",
                        color="black" if cm[i, j] > thresh else "black")
        fig.tight_layout()
        return ax

    # ---------------------------------------------------
    #   Function responsible for displaying the learning
    #   curve
    # ---------------------------------------------------
    def show_learning_curve(self, show=False):
        estimator = self.model.clf

        if self.model.grid_search:
            estimator = self.model.gs_clf

        self.plot_learning_curve(estimator, "Learning Curve (" + self.model.algorithm + ")",
                                 self.model.X_train, self.model.X_target, ylim=(0.0, 1.01), cv=5, n_jobs=1)
        if show:
            plt.show()
        else:
            return plt.gcf()

    # ---------------------------------------------------
    #   Function responsible for preparing the learning
    #   curve to be plotted
    # ---------------------------------------------------
    @staticmethod
    def plot_learning_curve(estimator, title, x, y, ylim=None, cv=None,
                            n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
        plt.figure()
        plt.title(title)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.xlabel("Training examples")
        plt.ylabel("Score")
        train_sizes, train_scores, test_scores = learning_curve(
            estimator, x, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)
        plt.grid()

        plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1, color="g")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")

        plt.legend(loc="best")
        return plt

    # ---------------------------------------------------
    #   Function responsible for displaying the ROC
    #   curve
    # ---------------------------------------------------
    def show_roc_curve(self, show=False):
        self.plot_roc_curve()

        if show:
            plt.show()
        else:
            return plt.gcf()

    # ---------------------------------------------------
    #   Function responsible for preparing the ROC
    #   curve to be plotted
    # ---------------------------------------------------
    def plot_roc_curve(self):
        y_score = self.model.get_y_score()

        # Compute ROC curve and ROC area
        fpr = dict()
        tpr = dict()
        roc_auc = dict()

        fpr[0], tpr[0], _ = roc_curve(np.array(self.model.test_dataset.get_evaluations()),
                                      y_score,
                                      pos_label='Positive')
        roc_auc[0] = auc(fpr[0], tpr[0])

        # Compute micro-average ROC curve and ROC area
        fpr["micro"], tpr["micro"], _ = roc_curve(np.array(self.model.test_dataset.get_evaluations()).ravel(),
                                                  y_score.ravel(),
                                                  pos_label='Positive')
        roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

        plt.figure()
        lw = 2
        plt.plot(fpr[0], tpr[0], color='darkorange',
                 lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[0])
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve (' + self.model.algorithm + ')')
        plt.legend(loc="lower right")

        return plt

    # ---------------------------------------------------
    #   Function responsible for displaying the
    #   precision-recall curve
    # ---------------------------------------------------
    def show_precision_recall_curve(self, show=False):
        self.plot_precision_recall_curve()

        if show:
            plt.show()
        else:
            return plt.gcf()

    # ---------------------------------------------------
    #   Function responsible for preparing the
    #   precision-recall curve to be plotted
    # ---------------------------------------------------
    def plot_precision_recall_curve(self):
        y_score = self.model.get_y_score()

        from sklearn.metrics import average_precision_score
        average_precision = average_precision_score(self.model.test_dataset.get_evaluations(),
                                                    y_score, pos_label='Positive')

        precision, recall, _ = precision_recall_curve(self.model.test_dataset.get_evaluations(),
                                                      y_score, pos_label='Positive')

        step_kwargs = ({'step': 'post'}
                       if 'step' in signature(plt.fill_between).parameters
                       else {})
        plt.step(recall, precision, color='b', alpha=0.2,
                 where='post')
        plt.fill_between(recall, precision, alpha=0.2, color='b', **step_kwargs)

        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.ylim([0.0, 1.05])
        plt.xlim([0.0, 1.0])
        plt.title('Precision-Recall Curve (' + self.model.algorithm + '): AP={0:0.2f}'.format(average_precision))

        return plt
