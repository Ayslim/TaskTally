from PyQt5 import QtWidgets
from program.view.generated.GeneratedMainWindow import Ui_MainWindow
from program.view.task_page import TaskPage
from program.view.statistics_page import StatisticsPage
from program.view.self_care_tips_page import SelfCareTipsPage
from program.view.info_page import InfoPage
from program.controller.task_list_controller import TaskListController

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        controller = TaskListController()
        taskPage = TaskPage(controller)
        statisticsPage = StatisticsPage(controller)
        selfCarePage = SelfCareTipsPage()
        infoPage = InfoPage()

        self.openTasksButton.clicked.connect(lambda: taskPage.show())
        self.openStatsButton.clicked.connect(lambda: statisticsPage.show())
        self.openSelfCareButton.clicked.connect(lambda: selfCarePage.show())
        self.openInfoButton.clicked.connect(lambda: infoPage.show())


