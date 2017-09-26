# codes_6.py

class MyForm(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        # Creating the grid that will position Widgets in a matrix
        # like manner
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        values = ['1', '2', '3',
                  '4', '5', '6',
                  '7', '8', '9',
                  '*', '0', '#']

        positions = [(i, j) for i in range(4) for j in range(3)]

        for _positions, value in zip(positions, values):
            if value == '':
                continue

            # The * symbol allows unpacking _positions as
            # independent arguments
            button = QtGui.QPushButton(value)
            grid.addWidget(button, *_positions)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
