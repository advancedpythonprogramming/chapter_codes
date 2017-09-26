# codes_9.py

import sys
from PyQt4 import QtGui, QtCore


class MySignal(QtCore.QObject):
    # This class defines the new signal 'signal_writer'
    signal_writer = QtCore.pyqtSignal()


class MyForm(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_GUI()

    def initialize_GUI(self):
        self.s = MySignal()
        self.s.signal_writer.connect(self.write_label)

        self.label1 = QtGui.QLabel('Label', self)
        self.label1.move(20, 10)
        self.resize(self.label1.sizeHint())

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Signal Emitter')
        self.show()

    def mousePressEvent(self, event):
        # This method handles when any of the mouse buttons is pressed. It is
        # defined by default within the app. It can be overwritten according
        # to how the event should be handled in each app.
        self.s.signal_writer.emit()

    def write_label(self):
        self.label1.setText('Mouse was clicked')
        self.label1.resize(self.label1.sizeHint())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
