from PyQt5 import QtWidgets

from program.view.generated.GeneratedStatisticsPage import Ui_Form

class StatisticsPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.close_btn.clicked.connect(self.close)

        self.updateProgressBar()
        
    def get_total_score(self):
        tasks = self.controller.fetch_from_firebase()
        return sum(task["score"] for task in tasks.values() if task["completed"])
    
    def getProgressBarValue(self):
        return int((self.get_total_score() / self.get_total_possible_points()) * 100)
    
    def updateProgressBar(self):
        self.progressBar.setValue(self.getProgressBarValue())
    
    def get_total_possible_points(self):
        tasks = self.controller.fetch_from_firebase()
        return sum(task["score"] for task in tasks.values())