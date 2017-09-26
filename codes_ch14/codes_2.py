# codes_2.py

from PyQt4 import QtGui


class MiForm(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        # Once the form is called, this method initializes the
        # interface and all of its elements and Widgets

        self.label1 = QtGui.QLabel('Text:', self)
        self.label1.move(10, 15)

        self.label2 = QtGui.QLabel('This label is modifiable', self)
        self.label2.move(10, 50)

        self.edit1 = QtGui.QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        # Adds all elements to the form
        self.setGeometry(200, 100, 200, 300)
        self.setWindowTitle('Window with buttons')


if __name__ == '__main__':
    app = QtGui.QApplication([])

    # A window that inherits from QMainWindow is created
    form = MiForm()
    form.show()
    app.exec_()
