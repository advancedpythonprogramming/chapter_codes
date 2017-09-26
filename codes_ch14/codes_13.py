# codes_13.py

from PyQt4 import QtGui, uic

form = uic.loadUiType("qt-designer-radiobutton.ui")
print(form[0], form[1])


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton1.clicked.connect(self.show_preferences)

    def show_preferences(self):
        for rb_id in range(1, 3):
            if getattr(self, 'radioButton' + str(rb_id)).isChecked():
                option = getattr(self, 'radioButton' + str(rb_id)).text()
                print(option)
                self.label2.setText('prefers: {0}'.format(option))
                self.label2.resize(self.label2.sizeHint())


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
