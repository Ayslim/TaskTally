# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 872)  # Set window size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Table Widget for displaying task statistics
        self.tbl_stats = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_stats.setGeometry(QtCore.QRect(160, 180, 501, 431))
        self.tbl_stats.setObjectName("tbl_stats")
        self.tbl_stats.setColumnCount(4)  # Define 4 columns
        self.tbl_stats.setRowCount(0)  # No rows initially
        self.tbl_stats.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Task Name"))
        self.tbl_stats.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Task Completed"))
        self.tbl_stats.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Date"))
        self.tbl_stats.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Streak"))

        # Progress Bar to show overall progress
        self.prg_points = QtWidgets.QProgressBar(self.centralwidget)
        self.prg_points.setGeometry(QtCore.QRect(880, 150, 321, 81))
        self.prg_points.setProperty("value", 24)  # Set initial progress value
        self.prg_points.setObjectName("prg_points")

        # List Widget for displaying weekly statistics
        self.lst_weeklyStats = QtWidgets.QListWidget(self.centralwidget)
        self.lst_weeklyStats.setGeometry(QtCore.QRect(890, 340, 291, 251))
        self.lst_weeklyStats.setObjectName("lst_weeklyStats")

        # Placeholder data for weekly stats 
        weekly_stats = [
            "Monday: 50 points",
            "Tuesday: 40 points",
            "Wednesday: 60 points",
            "Thursday: 30 points",
            "Friday: 70 points",
            "Saturday: 80 points",
            "Sunday: 0 points"
        ]
        self.lst_weeklyStats.addItems(weekly_stats)  # Add items to the weekly stats list

        # Buttons for closing the page and resetting progress
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(950, 710, 121, 31))
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setText("Close Page")
        self.btn_close.clicked.connect(MainWindow.close)  # Close window on click

        self.btn_resetStats = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resetStats.setGeometry(QtCore.QRect(1080, 710, 121, 31))
        self.btn_resetStats.setObjectName("btn_resetStats")
        self.btn_resetStats.setText("Reset Progress")
        self.btn_resetStats.clicked.connect(self.reset_stats)  # Connect reset function to button

        # Labels for different sections of the page
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(700, 70, 150, 31))
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_title.setText("Statistics")  # Title label

        self.lbl_overview = QtWidgets.QLabel(self.centralwidget)
        self.lbl_overview.setGeometry(QtCore.QRect(990, 200, 150, 31))
        self.lbl_overview.setObjectName("lbl_overview")
        self.lbl_overview.setText("Overall Progress")  # Overview label

        self.lbl_weekly_stats = QtWidgets.QLabel(self.centralwidget)
        self.lbl_weekly_stats.setGeometry(QtCore.QRect(990, 300, 150, 31))
        self.lbl_weekly_stats.setObjectName("lbl_weekly_stats")
        self.lbl_weekly_stats.setText("Weekly Tracker")  # Weekly stats label

        # Set the main layout, menu bar, and status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def reset_stats(self):
        """ Clears all statistics when the 'Reset Progress' button is clicked. """
        self.tbl_stats.setRowCount(0)  # Clear all rows in the statistics table
        self.prg_points.setValue(0)  # Reset progress bar to 0
        self.lst_weeklyStats.clear()  # Clear the weekly stats list

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  # Initialize the UI setup
    MainWindow.show()  # Display the window
    sys.exit(app.exec_())  # Execute the application
