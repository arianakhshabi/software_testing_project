from piece import *

class Bishop(ChessPiece):
    def valid_moves(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Check if the move is diagonal
        if abs(end_row - start_row) != abs(end_col - start_col):
            return False

        # Check if there are any pieces obstructing the diagonal path
        row_direction = 1 if end_row > start_row else -1
        col_direction = 1 if end_col > start_col else -1
        row = start_row + row_direction
        col = start_col + col_direction
        while row != end_row and col != end_col:
            if board[row][col] is not None:
                return False
            row += row_direction
            col += col_direction

        # Check if the destination square is empty or has an opponent's piece
        if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
            return True

        return False

    def __repr__(self):
        return '♝' if self.color == 'black' else '♗'
