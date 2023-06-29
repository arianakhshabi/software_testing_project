from piece import *

class Queen(ChessPiece):
    def valid_moves(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Check if the move is diagonal, horizontal, or vertical
        if abs(start_row - end_row) != abs(start_col - end_col) and start_row != end_row and start_col != end_col:
            return False

        # Check if there are any pieces obstructing the path
        if start_row == end_row:
            # Moving horizontally
            direction = 1 if end_col > start_col else -1
            for col in range(start_col + direction, end_col, direction):
                if board[start_row][col] is not None:
                    return False
        elif start_col == end_col:
            # Moving vertically
            direction = 1 if end_row > start_row else -1
            for row in range(start_row + direction, end_row, direction):
                if board[row][start_col] is not None:
                    return False
        else:
            # Moving diagonally
            row_direction = 1 if end_row > start_row else -1
            col_direction = 1 if end_col > start_col else -1
            row = start_row + row_direction
            col = start_col + col_direction
            while row != end_row:
                if board[row][col] is not None:
                    return False
                row += row_direction
                col += col_direction

        # Check if the destination square is empty or has an opponent's piece
        if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
            return True

        return False

    def __repr__(self):
        return '♛' if self.color == 'black' else '♕'