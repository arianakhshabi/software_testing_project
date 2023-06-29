# Chess Game

class ChessPiece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, start, end, board):
        raise NotImplementedError("Subclass must implement the valid_moves method")

    def __repr__(self):
        raise NotImplementedError("Subclass must implement the __repr__ method")

class King(ChessPiece):
    def valid_moves(self, start, end, board):
        # Implement logic for valid king moves
        pass

    def __repr__(self):
        return '♚' if self.color == 'black' else '♔'

class Queen(ChessPiece):
    def valid_moves(self, start, end, board):
        # Implement logic for valid queen moves
        pass

    def __repr__(self):
        return '♛' if self.color == 'black' else '♕'

class Rook(ChessPiece):
    def valid_moves(self, start, end, board):
        # Implement logic for valid rook moves
        pass

    def __repr__(self):
        return '♜' if self.color == 'black' else '♖'

class Bishop(ChessPiece):
    def valid_moves(self, start, end, board):
        # Implement logic for valid bishop moves
        pass

    def __repr__(self):
        return '♝' if self.color == 'black' else '♗'

class Knight(ChessPiece):
    def valid_moves(self, start, end, board):
        # Implement logic for valid knight moves
        pass

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
        self.board[start[0]][start[1]] = None
        self.board[end[0]][end[1]] = piece
        move = ChessMove(start, end)
        self.moves.append(move)

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
