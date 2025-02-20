# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import pickle


class Ui_TaskPage(object):
    def setupUi(self, TaskPage):
        TaskPage.setObjectName("TaskPage")
        TaskPage.resize(800, 600)

        # Create a central widget for the task page
        self.centralwidget = QtWidgets.QWidget(TaskPage)
        self.centralwidget.setObjectName("centralwidget")
        
        # Points label to display the user's score
        self.pointsLabel = QtWidgets.QLabel(self.centralwidget)
        self.pointsLabel.setGeometry(QtCore.QRect(920, 110, 60, 16))
        self.pointsLabel.setObjectName("pointsLabel")
        
        # Label for the "To-Do" list heading
        self.toDoLabel = QtWidgets.QLabel(self.centralwidget)
        self.toDoLabel.setGeometry(QtCore.QRect(660, 90, 81, 31))
        self.toDoLabel.setObjectName("toDoLabel")
        
        # Reset button that clears tasks and resets points
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(850, 620, 131, 31))
        self.resetButton.setObjectName("resetButton")
        
        # Save button that stores progress to a file
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(850, 590, 131, 31))
        self.saveButton.setObjectName("saveButton")
        
        # Task list view using QListWidget with checkboxes for each task
        self.taskList = QtWidgets.QListWidget(self.centralwidget)
        self.taskList.setGeometry(QtCore.QRect(440, 150, 551, 411))
        self.taskList.setObjectName("taskList")
        self.taskList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)  # Enable multiple selection (checkboxes)
        
        # Predefined tasks to be displayed in the task list
        premade_tasks = [
            "Task 1: Learn Python",
            "Task 2: Complete homework",
            "Task 3: Study for exam",
            "Task 4: Organize desk",
            "Task 5: Read a book"
        ]
        
        # Add each task to the list with an initial unchecked state
        for task in premade_tasks:
            item = QtWidgets.QListWidgetItem(task)
            item.setCheckState(QtCore.Qt.Unchecked)  # Initially unchecked
            self.taskList.addItem(item)
        
        # Connect the itemChanged signal to the updatePoints function
        self.taskList.itemChanged.connect(self.updatePoints)

        # Set the central widget for the main window
        TaskPage.setCentralWidget(self.centralwidget)
        
        # Menu bar (currently empty but can be populated later if needed)
        self.menubar = QtWidgets.QMenuBar(TaskPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        TaskPage.setMenuBar(self.menubar)
        
        # Status bar (for displaying messages)
        self.statusbar = QtWidgets.QStatusBar(TaskPage)
        self.statusbar.setObjectName("statusbar")
        TaskPage.setStatusBar(self.statusbar)

        # Set the window title and labels using retranslateUi method
        self.retranslateUi(TaskPage)
        QtCore.QMetaObject.connectSlotsByName(TaskPage)

    def retranslateUi(self, TaskPage):
        """Set the window title and text for labels and buttons."""
        _translate = QtCore.QCoreApplication.translate
        TaskPage.setWindowTitle(_translate("TaskPage", "Task Page"))
        self.pointsLabel.setText(_translate("TaskPage", "Points: 0"))
        self.toDoLabel.setText(_translate("TaskPage", "TO-DO LIST"))
        self.resetButton.setText(_translate("TaskPage", "Reset Everything"))
        self.saveButton.setText(_translate("TaskPage", "Save Progress"))

    def saveProgress(self):
        """Save the progress (task states and points) to a file using pickle."""
        # Create a dictionary with tasks and points to store
        data = {
            'tasks': [(self.taskList.item(i).text(), self.taskList.item(i).checkState()) for i in range(self.taskList.count())],
            'points': self.pointsLabel.text().split(': ')[1]  # Extract points from the label
        }
        
        # Write the data to a file (task_progress.pkl)
        with open('task_progress.pkl', 'wb') as file:
            pickle.dump(data, file)

    def loadProgress(self):
        """Load saved progress (tasks and points) from a file."""
        try:
            # Try to load saved progress from file
            with open('task_progress.pkl', 'rb') as file:
                data = pickle.load(file)
                tasks = data.get('tasks', [])
                points = data.get('points', '0')
                
                # Clear the current tasks before loading new ones
                self.taskList.clear()
                
                # Add the saved tasks back to the list with their respective check states
                for task, checkState in tasks:
                    item = QtWidgets.QListWidgetItem(task)
                    item.setCheckState(checkState)  # Set the saved check state for each task
                    self.taskList.addItem(item)
                    
                # Set the points label based on the saved points
                self.pointsLabel.setText(f"Points: {points}")
        except FileNotFoundError:
            # If no saved progress file exists, do nothing
            pass

    def resetEverything(self):
        """Clear all tasks and reset points to zero."""
        self.taskList.clear()
        self.pointsLabel.setText("Points: 0")

    def updatePoints(self):
        """Update the points based on the number of tasks checked."""
        points = 0
        for i in range(self.taskList.count()):
            if self.taskList.item(i).checkState() == QtCore.Qt.Checked:
                points += 1  # Add 1 point for each checked task
        self.pointsLabel.setText(f"Points: {points}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaskPage = QtWidgets.QMainWindow()
    ui = Ui_TaskPage()
    ui.setupUi(TaskPage)
    ui.loadProgress()  # Load progress when the application starts
    TaskPage.show()
    sys.exit(app.exec_())
