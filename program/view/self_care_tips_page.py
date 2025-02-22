from PyQt5 import QtWidgets

from program.view.generated.GeneratedSelfCareTipsPage import Ui_Form

class SelfCareTipsPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.previousPageBtn.clicked.connect(self.goPrevious)
        self.nextPageBtn.clicked.connect(self.goNext)

    def goPrevious(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index > 0:
            self.stackedWidget.setCurrentIndex(current_index - 1)   

    def goNext(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(current_index + 1)
       


