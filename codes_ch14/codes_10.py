# codes_10.py

def keyPressEvent(self, event):
    self.statusBar().showMessage('Key pressed {}'.format(event.text()))


def mousePressEvent(self, *args, **kwargs):
    self.statusBar().showMessage('Mouse click')
