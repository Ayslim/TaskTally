from PyQt5 import QtWidgets, QtCore
from program.view.generated.GeneratedTaskPage import Ui_Form

class TaskPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        # Don't update this variable, just use it to look up scores
        self.data_from_db = controller.fetch_from_firebase()

        for task_description, task_data in self.data_from_db.items():
            checked = task_data["completed"]
            label = f"({task_data["score"]}) {task_description}"
            item = QtWidgets.QListWidgetItem(label)
            item.setCheckState(QtCore.Qt.Unchecked if not checked else QtCore.Qt.Checked)
            self.taskListView.addItem(item)

        self.resetAllTasksBtn.clicked.connect(self.resetAllTasks)
        self.taskListView.itemChanged.connect(self.taskUpdated)
        self.updateTotalScore()
    
    # Updates each item in the list, which causes taskUpdated() to be run, which updates the total score and the completed status in the db
    def resetAllTasks(self):
        for item in self.get_list_items():
            item.setCheckState(QtCore.Qt.Unchecked)

    def taskUpdated(self, item):
        task_description, checked = self.getTextAndChecked(item)
        self.controller.set_in_firebase(task_description, checked)
        self.updateTotalScore()

    def updateTotalScore(self):
        score = 0
        for item in self.get_list_items():
            task_description, checked = self.getTextAndChecked(item)
            if(checked):
                score += self.data_from_db[task_description]["score"]
        self.totalScore.setText(str(score))

    def getTextAndChecked(self, item):
        # Split on the space between points and task description. Only do one split, and get the second element in the result (task description)
        task_description = item.text().split(" ", 1)[1]
        checked = True if item.checkState() == QtCore.Qt.CheckState.Checked else False
        return task_description, checked
    
    def get_list_items(self):
        return [self.taskListView.item(x) for x in range(self.taskListView.count())]
        
       

