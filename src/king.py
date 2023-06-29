from piece import *

class King(ChessPiece):
    def valid_moves(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Check if the move is within one square in any direction
        if abs(start_row - end_row) > 1 or abs(start_col - end_col) > 1:
            return False

        # Check if the destination square is empty or has an opponent's piece
        if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
            return True

        return False

    def __repr__(self):
        return '♚' if self.color == 'black' else '♔'
