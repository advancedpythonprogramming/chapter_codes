# codes_4.py

from PyQt4 import QtGui


class MainForm(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()

        # Configures window geometry
        self.setWindowTitle('Window with buttons')
        self.setGeometry(200, 100, 300, 250)

        # Action definitions
        see_status = QtGui.QAction(QtGui.QIcon(None), '&Change '
                                                      'Status', self)
        see_status.setStatusTip('This is a test item')
        see_status.triggered.connect(self.change_status_bar)

        exit = QtGui.QAction(QtGui.QIcon(None), '&Exit', self)
        # We can define a key combination to execute each command
        exit.setShortcut('Ctrl+Q')
        # This method shows the command description on the status bar
        exit.setStatusTip('End the app')
        # Connects the signal to the slot that will handle this event
        exit.triggered.connect(QtGui.qApp.quit)

        # Menu and menu bar creation
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')  # first menu
        file_menu.addAction(see_status)
        file_menu.addAction(exit)

        other_menu = menubar.addMenu('&Other Menu')  # second menu

        # Includes the status bar
        self.statusBar().showMessage('Ready')

        # Sets the previously created form as the central widged
        self.form = MyForm()
        self.setCentralWidget(self.form)

    def change_status_bar(self):
        self.statusBar().showMessage('Status has been changed')


class MyForm(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        self.label1 = QtGui.QLabel('Text:', self)
        self.label1.move(10, 15)

        self.label2 = QtGui.QLabel('Write the answer here', self)
        self.label2.move(10, 50)

        self.edit1 = QtGui.QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        self.button1 = QtGui.QPushButton('&Process', self)
        self.button1.resize(self.button1.sizeHint())
        self.button1.move(5, 70)

        self.setGeometry(200, 100, 200, 300)
        self.setWindowTitle('Window with buttons')
        self.show()

    def button_pressed(self):
        sender = self.sender()
        self.label3.setText('Signal origin: {0}'.format(sender.text()))
        self.label3.resize(self.label3.sizeHint())

    def button1_callback(self):
        self.label2.setText('{}'.format(self.edit1.text()))
        self.label2.resize(self.label2.sizeHint())


if __name__ == '__main__':
    app = QtGui.QApplication([])

    form = MainForm()
    form.show()
    app.exec_()
