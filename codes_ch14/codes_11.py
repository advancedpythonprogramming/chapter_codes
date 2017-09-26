# codes_11.py

from PyQt4 import QtGui, uic

form = uic.loadUiType("qt-designer-label.ui")


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Interface is initialized


if __name__ == '__main__':
    # Application should be initialized just as if it had been
    # created manually
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
