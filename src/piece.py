class ChessPiece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, start, end, board):
        raise NotImplementedError("Subclass must implement the valid_moves method")

    def __repr__(self):
        raise NotImplementedError("Subclass must implement the __repr__ method")
