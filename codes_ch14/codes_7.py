# codes_7.py

class MyForm(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        self.label1 = QtGui.QLabel('Text:', self)
        self.label1.move(10, 15)

        self.label2 = QtGui.QLabel('Write your answer here', self)
        self.label2.move(10, 50)

        self.edit1 = QtGui.QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        # Connecting button1 signal to other object
        self.button1 = QtGui.QPushButton('&Process', self)
        self.button1.resize(self.button1.sizeHint())
        self.button1.move(5, 70)
        # This object MUST be callable. self.button1_callback()
        # would not work.
        self.button1.clicked.connect(self.button1_callback)

        self.button2 = QtGui.QPushButton('&Exit', self)
        self.button2.clicked.connect(
            QtCore.QCoreApplication.instance().quit)
        self.button2.resize(self.button2.sizeHint())
        self.button2.move(90, 70)

        self.setGeometry(200, 100, 200, 300)
        self.setWindowTitle('Window with buttons')

    def button1_callback(self):
        # This method handles the event
        self.label2.setText(self.edit1.text())
