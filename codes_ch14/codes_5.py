# codes_5.py

from PyQt4 import QtGui


class MainForm(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()

        # Window geometry
        self.setWindowTitle('Window with buttons')
        self.setGeometry(200, 100, 300, 250)

        self.form = MiForm()
        self.setCentralWidget(self.form)


class MiForm(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        self.label1 = QtGui.QLabel('Text:', self)
        self.label1.move(10, 15)

        self.edit1 = QtGui.QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        self.button1 = QtGui.QPushButton('&Calculate', self)
        self.button1.resize(self.button1.sizeHint())

        # QHBoxLayout() and QVBoxLayout() are created and added to the
        # Widget list by using the addWidget() method. The stretch()
        # method includes a spacing that expands the layout towards
        #  the right and downwards.
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.edit1)
        hbox.addWidget(self.button1)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # The vertical layout contains the horizontal layout
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QtGui.QApplication([])

    form = MainForm()
    form.show()
    app.exec_()
