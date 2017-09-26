# codes_12.py

from PyQt4 import QtGui, uic

form = uic.loadUiType("qt-designer-mainwindow.ui")
print(form[0], form[1])


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        # QtDesigner created interface is initialized
        self.setupUi(self)

        # Button signal is connected
        self.pushButton1.clicked.connect(self.divide)

    def divide(self):
        # This function acts as a slot for de button clicked signal
        self.label_3.setText('= ' + str(
            float(self.lineEdit1.text()) / float(
                self.lineEdit2.text())))


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
