# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from taskPage import Ui_TaskPage  # Assuming this is the task page class
from info import Ui_background
from self_care_tips import Ui_background


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(560, 360, 301, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.openStatsButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openStatsButton.setObjectName("openStatsButton")
        self.gridLayout.addWidget(self.openStatsButton, 1, 0, 1, 1)
        
        self.openSelfCareButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openSelfCareButton.setObjectName("openSelfCareButton")
        self.gridLayout.addWidget(self.openSelfCareButton, 0, 0, 1, 1)
        
        self.openTasksButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openTasksButton.setObjectName("openTasksButton")
        self.gridLayout.addWidget(self.openTasksButton, 0, 1, 1, 1)
        
        self.openInfoButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openInfoButton.setObjectName("openInfoButton")
        self.gridLayout.addWidget(self.openInfoButton, 1, 1, 1, 1)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 280, 61, 41))
        self.label.setObjectName("label")  # "TaskTally" label
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 530, 60, 16))
        self.label_2.setObjectName("label_2")  # "Points: 0" label
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openStatsButton.setText(_translate("MainWindow", "Statistics"))
        self.openSelfCareButton.setText(_translate("MainWindow", "Self Care Tips"))
        self.openTasksButton.setText(_translate("MainWindow", "To-Do List"))
        self.openInfoButton.setText(_translate("MainWindow", "Info Page"))
        self.label.setText(_translate("MainWindow", "TaskTally"))
        self.label_2.setText(_translate("MainWindow", "Points: 0"))

    def openTaskPage(self):
        """Function to open the task page when the button is clicked."""
        self.taskPage = QtWidgets.QMainWindow()
        self.ui_taskPage = Ui_TaskPage()  # Instantiate the task page class
        self.ui_taskPage.setupUi(self.taskPage)
        self.taskPage.show()

    def openInfoPage(self):
        """Function to open the info page when the button is clicked."""
        self.infoPage = QtWidgets.QMainWindow()
        self.ui_infoPage = Ui_background()  # Instantiate the Info page class
        self.ui_infoPage.setupUi(self.infoPage)
        self.infoPage.show()

    def connectSignals(self):
        """Connect all signals (button clicks) to appropriate functions."""
        self.openTasksButton.clicked.connect(self.openTaskPage)  # Open task page when button is clicked
        self.openInfoButton.clicked.connect(self.openInfoPage)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connectSignals()  # Connect signals after the UI setup
    MainWindow.show()
    sys.exit(app.exec_())
