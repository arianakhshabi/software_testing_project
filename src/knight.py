from piece import *

class Knight(ChessPiece):
    def valid_moves(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Calculate the difference in rows and columns
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Check if the move is a valid knight move
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            destination_piece = board[end_row][end_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True

        return False

    def __repr__(self):
        return '♞' if self.color == 'black' else '♘'
