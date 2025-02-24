from PyQt5 import QtWidgets

from program.view.generated.GeneratedStatisticsPage import Ui_Form

class StatisticsPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.close_btn.clicked.connect(self.close)
       

