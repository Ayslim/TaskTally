from PyQt5 import QtWidgets, QtCore
from program.view.generated.GeneratedTaskPage import Ui_Form

class TaskPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self, controller, statistics_page):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.controller = controller
        self.statistics_page = statistics_page

        # Don't update this variable, just use it to look up scores
        self.data_from_db = controller.fetch_from_firebase()

        #task_data is the value for the task key.
        for task_description, task_data in self.data_from_db.items():
            task_completed = task_data["completed"]
            score = task_data["score"]
            label = f"({score}) {task_description}"
            item = QtWidgets.QListWidgetItem(label)
            item.setCheckState(QtCore.Qt.Checked if task_completed else QtCore.Qt.Unchecked)
            self.taskListView.addItem(item)

        self.resetAllTasksBtn.clicked.connect(self.resetAllTasks)
        self.taskListView.itemChanged.connect(self.taskUpdated)
        self.customTaskBtn.clicked.connect(self.taskAdded)
        self.updateTotalScore()
        self.statistics_page.updateProgressBar()  # Ensure it's updated initially

    # Updates each item in the list, which causes taskUpdated() to be run, which updates the total score and the completed status in the db
    def resetAllTasks(self):
        for item in self.get_list_of_QListWidgetItems():
            item.setCheckState(QtCore.Qt.Unchecked)
        self.statistics_page.updateProgressBar()  # Update progress bar after reset

    # The task wask checked or unchecked in the UI. Let's update the completed status in the database, and update the total score label
    def taskUpdated(self, item):
        task_description, checked = self.getTaskDescriptionAndCheckedStatusFromQListWidgetItem(item)
        # Setting the checked status in the database using the controller
        self.controller.set_completed_status_on_task(task_description, checked)
        self.updateTotalScore()
        self.statistics_page.updateProgressBar() 
    
    def updateTotalScore(self):
        score = 0
        for item in self.get_list_of_QListWidgetItems():
            task_description, checked = self.getTaskDescriptionAndCheckedStatusFromQListWidgetItem(item)
            if(checked):
                score += self.data_from_db[task_description]["score"]
        self.totalScore.setText(str(score))
        self.statistics_page.updateProgressBar() 
    
    # Getting the task description and checked status from the QListWidget (not the db!) 
    def getTaskDescriptionAndCheckedStatusFromQListWidgetItem(self, item):
        # Split on the space between points and task description. Only do one split, and get the second element in the result (task description)
        # (20)> <Clean your room
        task_description = item.text().split(" ", 1)[1]
        checked = True if item.checkState() == QtCore.Qt.CheckState.Checked else False
        return task_description, checked
    
    def get_list_of_QListWidgetItems(self):
        # There is no easy way to get all the items from the QListWidget
        # This is a list comprehension that gets item 0, item 1, item 2, etc.
        # This returns a list of QListWidgetItem
        return [self.taskListView.item(x) for x in range(self.taskListView.count())]
    
    def taskAdded(self):
        customTaskDescription = self.customTaskDescription.text()
        customTaskPoints = self.customTaskPoints.value()

        self.customTaskDescription.clear()
        self.customTaskPoints.clear()

        self.controller.addTaskToDatabase(customTaskDescription, customTaskPoints)

        self.data_from_db[customTaskDescription] = {"completed": False, "score": customTaskPoints}

        label = f"({customTaskPoints}) {customTaskDescription}"
        item = QtWidgets.QListWidgetItem(label)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskListView.addItem(item)

        self.statistics_page.updateProgressBar()  # Update progress bar after new task is added
