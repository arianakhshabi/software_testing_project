from piece import *

class Rook(ChessPiece):
    def valid_moves(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Check if the move is horizontal or vertical
        if start_row != end_row and start_col != end_col:
            return False

        # Check if there are any pieces obstructing the path
        if start_row == end_row:
            # Moving horizontally
            direction = 1 if end_col > start_col else -1
            for col in range(start_col + direction, end_col, direction):
                if board[start_row][col] is not None:
                    return False
        else:
            # Moving vertically
            direction = 1 if end_row > start_row else -1
            for row in range(start_row + direction, end_row, direction):
                if board[row][start_col] is not None:
                    return False

        # Check if the destination square is empty or has an opponent's piece
        if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
            return True

        return False

    def __repr__(self):
        return '♜' if self.color == 'black' else '♖'