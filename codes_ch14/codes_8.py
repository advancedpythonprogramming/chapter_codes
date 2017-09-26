# codes_8.py

def init_GUI(self):
    self.label1 = QtGui.QLabel('Text:', self)
    self.label1.move(10, 15)

    self.label2 = QtGui.QLabel('Write your answer here:', self)
    self.label2.move(10, 50)

    self.label3 = QtGui.QLabel('Signal origin:', self)
    self.label3.move(10, 250)

    self.edit1 = QtGui.QLineEdit('', self)
    self.edit1.setGeometry(45, 15, 100, 20)

    self.button1 = QtGui.QPushButton('&Process', self)
    self.button1.resize(self.button1.sizeHint())
    self.button1.move(5, 70)
    self.button1.clicked.connect(self.button1_callback)
    self.button1.clicked.connect(self.button_pressed)

    self.button2 = QtGui.QPushButton('&Exit', self)
    self.button2.clicked.connect(QtCore.QCoreApplication.instance().quit)
    self.button2.resize(self.button2.sizeHint())
    self.button2.move(90, 70)

    self.setGeometry(200, 100, 300, 300)
    self.setWindowTitle('Window with buttons.')
    self.show()


def button_pressed(self):
    # This method registers the object sending the signal and shows it in
    # label3 by using the sender() method
    sender = self.sender()
    self.label3.setText('Signal origin: {0}'.format(sender.text()))
    self.label3.resize(self.label3.sizeHint())


def button1_callback(self):
    self.label2.setText(self.edit1.text())
