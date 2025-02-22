from PyQt5 import QtWidgets

from program.view.generated.GeneratedInfoPage import Ui_Form

class InfoPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("GOOD MOOOOORNIIIIING\nAGAAAAIN")
       


