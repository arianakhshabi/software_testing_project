import copy

class ChessPiece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, start, end, board):
        raise NotImplementedError("Subclass must implement the valid_moves method")

    def __repr__(self):
        raise NotImplementedError("Subclass must implement the __repr__ method")

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

class Knight(ChessPiece):
    def valid_moves(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Calculate the difference in rows and columns
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Check if the move is a valid knight move
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return True

        return False

    def __repr__(self):
        return '♞' if self.color == 'black' else '♘'

class Pawn(ChessPiece):
    
    def valid_moves(self, start, end, board):
    
        start_row, start_col = start
        end_row, end_col = end
        print(start_row,end_row)

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


   

class ChessMove:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Move: {self.start} to {self.end}"

class ChessGame:
    def __init__(self):
        self.board = [
            [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')],
            [Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')],
            [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
        ]
        self.current_player = 'white'
        self.moves = []
        self.previous_board = None  # Store moves history for undo


    def print_board(self):
        for row in self.board:
            print(' '.join(str(piece) if piece is not None else ' ' for piece in row))
        print()

    
    def is_valid_move(self, start, end):
        start_row, start_col = start
        piece = self.board[start_row][start_col]
        if piece is None:
            return False

        # Check if it is the player's turn to move
        if (self.current_player == 'white' and piece.color != 'white') or (self.current_player == 'black' and piece.color != 'black'):
            return False

        return piece.valid_moves(start, end, self.board)

    
    def make_move(self, start, end):
        piece = self.board[start[0]][start[1]]
        self.previous_board = copy.deepcopy(self.board)  # Store the previous board state
        self.board[start[0]][start[1]] = None
        self.board[end[0]][end[1]] = piece
        move = ChessMove(start, end)
        self.moves.append(move)

    def undo_move(self):
        if len(self.moves) == 0:
            print("No moves to undo.")
            return

        last_move = self.moves.pop()
        
        self.board = self.previous_board  # Restore the previous board state
        self.previous_board = None  # Clear the previous board state
        self.current_player = 'white' if self.current_player == 'black' else 'black'  # Switch the current player
        print("Undo successful.")
        print("Last move:", last_move)

    def play_game(self):
        while True:
            self.print_board()

            print(f"It's {self.current_player}'s turn.")

            # Get move input from the current player
            action = input("Chose 'm' for move or 'r' to reset q for quit and u for undo : ")

            if action == 'r':
                self.reset_board()
                continue
            elif action=='q':
                exit()
            if action == 'u':
                self.undo_move()
                continue

            # Split the input into start and end positions
            elif action=='m':
                start = input("Enter the starting position (e.g., 'a2'): ")
                end = input("Enter the ending position (e.g., 'a4'): ")

                # Convert input to board indices
                start = (8 - int(start[1]), ord(start[0]) - ord('a') )
                end = (8 - int(end[1]), ord(end[0]) - ord('a') )


                # Check if the move is valid
                piece = self.is_valid_move(start, end)
                if piece:
                    self.make_move(start, end)
                    self.current_player = 'black' if self.current_player == 'white' else 'white'
                else:
                    print("Invalid move! Try again.")


    def reset_board(self):
        self.board = [
            [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')],
            [Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')],
            [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
        ]
        self.current_player = 'white'
        self.moves = []


# Create an instance of the ChessGame class and start the game
game = ChessGame()
game.play_game()
