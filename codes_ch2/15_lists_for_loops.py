class Piece:
    # Avoid using id as variable because it is a reserved word
    pid = 0

    def __init__(self, piece):
        Piece.pid += 1
        self.pid = Piece.pid
        self.type = piece

pieces = []
pieces.append(Piece('Bishop'))
pieces.append(Piece('Pawn'))
pieces.append(Piece('King'))
pieces.append(Piece('Queen'))

for piece in pieces:
    print('pid: {0} - types of piece: {1}'.format(piece.pid, piece.type))
