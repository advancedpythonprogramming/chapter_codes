# codes_1.py

from PyQt4 import QtGui


class MiForm(QtGui.QWidget):
    # The next line defines the window geometry.
    # Parameters: (x_top_left, y_top_left, width, height)
    self.setGeometry(200, 100, 300, 300)
    self.setWindowTitle('My First Window')  # Optional


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MiForm()
    form.show()
    app.exec_()
