from piece import *


class Pawn(ChessPiece):
    
    def valid_moves(self, start, end, board):
    
        start_row, start_col = start
        end_row, end_col = end
        

        direction = -1 if self.color == 'white' else 1

        # Check if the move is a valid pawn move
        if end_col == start_col and end_row == start_row + direction and board[end_row][end_col] is None:
            return True
        elif end_row == start_row + direction and abs(end_col - start_col) == 1 and board[end_row][end_col] is not None:
            return True
        elif start_row == 1 and end_row == start_row + 2 * direction and start_col == end_col and board[start_row + direction][start_col] is None and board[end_row][end_col] is None:
            return True
        elif start_row == 6 and end_row == start_row + 2 * direction and start_col == end_col and board[start_row + direction][start_col] is None and board[end_row][end_col] is None:
            return True

        return False


    def __repr__(self):
        return '♟' if self.color == 'black' else '♙'


