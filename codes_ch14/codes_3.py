# codes_3.py

from PyQt4 import QtGui


class MyForm(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        # Once the form is called, this method initializes the
        # interface and all of its elements and Widgets
        self.label1 = QtGui.QLabel('Text:', self)
        self.label1.move(10, 15)

        self.label2 = QtGui.QLabel('Write the answer here', self)
        self.label2.move(10, 50)

        self.edit1 = QtGui.QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        # The use of the & symbol at the start of the text within
        # any button or menu makes it so the first letter is shown
        # in bold font. This visualization may depend on the used
        # platform.
        self.button1 = QtGui.QPushButton('&Process', self)
        self.button1.resize(self.button1.sizeHint())
        self.button1.move(5, 70)

        # Adds all elements to the form
        self.setGeometry(200, 100, 200, 300)
        self.setWindowTitle('Window with buttons')
        self.show()


if __name__ == '__main__':
    app = QtGui.QApplication([])

    # A window that inherits from QMainWindow is created
    form = MyForm()
    form.show()
    app.exec_()
