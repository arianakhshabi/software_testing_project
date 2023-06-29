class ChessMove:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Move: {self.start} to {self.end}"
