import sys
from PyQt5 import QtWidgets
from program.view.main_window import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())