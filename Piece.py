class Piece:
    def __init__(self, player, piece , Board):
        self.name = ""
        self.number_of_pieces = -1
        self.pos = {"x": -1, "y": -1}
        self.player = player
        self.piece = piece
        self.Board = Board