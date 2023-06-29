import copy

from colorama import Fore

from piece import *

from king import*
from queen import*
from rook import*
from bishop import*
from knight import*
from pawn import*

from move import*


   


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
             print(' '.join((Fore.GREEN+str(piece)+Fore.WHITE) if piece is not None and piece.color == "white" else (Fore.BLUE+str(piece)+Fore.WHITE) if piece is not None else ' ' for piece in row))
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

    def calculate_possible_moves(self, row, col,board):
        piece = self.board[row][col]

        # Check if a piece exists at the given position
        if piece is None:
            return []

        # Initialize a list to store the possible moves
        possible_moves = []

        # Chess notation mapping for columns
        column_mapping = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        # Iterate over all the board positions
        for i in range(8):
            for j in range(8):
                end = (i, j)

                # Check if the move is valid
                if piece.valid_moves((row, col), end, self.board):
                    # Convert row and column indices to chess notation
                    start_position = f"{column_mapping[col]}{8 - row}"
                    end_position = f"{column_mapping[j]}{8 - i}"

                    possible_moves.append((start_position, end_position))

        return possible_moves


    def is_check(self, player_color):
    # Find the position of the player's king
        king_position = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == player_color:
                    king_position = (row, col)
                    break

        if king_position is None:
            return False

        # Check if any opponent's piece can attack the king
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color != player_color:
                    start = (row, col)
                    for i in range(8):
                        for j in range(8):
                            end = (i, j)
                            if self.is_valid_move(start, end) and self.board[row][col].valid_moves(start, end, self.board):
                                return True

        return False




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

                possible_moves = self.calculate_possible_moves(start[0], start[1], self.board)
                print(possible_moves)
                # Check if the move is valid
                piece = self.is_valid_move(start, end)
                if piece:
                    self.make_move(start, end)
                    self.current_player = 'black' if self.current_player == 'white' else 'white'
                    if self.is_check("black"if (self.current_player == "white") else "white"):
                        print(f"{Fore.RED}{self.current_player} is in check!{Fore.WHITE}")
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
def test_chess_game():
    game = ChessGame()
###############################################################################test magadir avaliye board#########################
    # Test initial board state
    if str(game.board[0][4]) == '♚':
        print(f"{Fore.GREEN}ok Black King{Fore.WHITE}")  # Test for Black King
    else :
        print(f"{Fore.RED}NOT OK {Fore.WHITE}")


    if str(game.board[7][4]) == '♔' :
        print(f"{Fore.GREEN}ok White King{Fore.WHITE}") # White King
    else :
        print(f"{Fore.RED}NOT OK {Fore.WHITE}")


    if str(game.board[0][0]) == '♜':
        print(f"{Fore.GREEN}ok black rook{Fore.WHITE}")
    else :
        print(f"{Fore.RED}NOT OK {Fore.WHITE}") 

 
    if str(game.board[7][7]) == '♖':
          print(f"{Fore.GREEN}ok white rook{Fore.WHITE}")# White Rook
    else :
        print(f"{Fore.RED}NOT OK {Fore.WHITE}")


############################################################## test harekat ha  pawn #######################################################
    game.make_move((6, 4), (4, 4))
    if  str(game.board[4][4]) == '♙':
        if  str(game.board[6][4])=="None":
            print(f"{Fore.GREEN}this move is ok{Fore.WHITE}")
    else :
        print(f"{Fore.RED}NOT OK {Fore.WHITE}")
    
#################################################### test harekat knight   ################################################################
    game.make_move((7, 6), (5, 5))
    if str(game.board[5][5]) == '♘':
        if str(game.board[7][6]) == "None":
            print(f"{Fore.GREEN}This move is valid.{Fore.WHITE}")
        else:
            print(f"{Fore.RED}This move is invalid. Destination position is not empty.{Fore.WHITE}")
    else:
        print(f"{Fore.RED}This move is invalid. Starting position does not contain a knight.{Fore.WHITE}")

    game.make_move((1, 0), (2, 2))
    if str(game.board[2][2]) == '♞':
        if str(game.board[1][0]) == "None":
            print(f"{Fore.GREEN}This move is valid.{Fore.WHITE}")
        else:
            print(f"{Fore.RED}This move is invalid. Destination position is not empty.{Fore.WHITE}")
    else:
        print(f"{Fore.RED}This move is invalid. {Fore.GREEN} so Logics worked correctly.{Fore.WHITE} sarbaz be (2,2) nemiravad")
    
    game.make_move((1, 0), (3, 1))
    if str(game.board[3][1]) == '♞':
        if str(game.board[1][0]) == "None":
            print(f"{Fore.GREEN}This move is valid.{Fore.WHITE}")
        else:
            print(f"{Fore.RED}This move is invalid. Destination position is not empty.{Fore.WHITE}")
    else:
        print(f"{Fore.RED}This move is invalid. {Fore.GREEN} so Logics worked correctly.{Fore.WHITE}")

    game.make_move((3, 4), (3, 3))
    if str(game.board[3][2]) == '♞':
        if str(game.board[3][2]) == "None":
            print(f"{Fore.GREEN}This move is valid.{Fore.WHITE}")
        else:
            print(f"{Fore.RED}This move is invalid. Destination position is not empty.{Fore.WHITE}")
    else:
        print(f"{Fore.RED}This move is invalid. {Fore.GREEN} so Logics worked correctly.{Fore.WHITE}")



    game.make_move((0, 1), (2, 0))
    if str(game.board[2][0]) == '♞':
        if str(game.board[0][1]) == "None":
            print(f"{Fore.GREEN}This move is valid.{Fore.WHITE}")
        else:
            print(f"{Fore.RED}This move is invalid. Destination position is not empty.{Fore.WHITE}")
    else:
        print(f"{Fore.RED}This move is invalid. Starting position does not contain a knight.{Fore.WHITE}")


   

########################################################### test undo ##########################################################

    game.undo_move()
    if str(game.board[0][1]) == '♞':
        if str(game.board[2][0]) == "None":
            print(f"{Fore.GREEN}This move is valid.{Fore.WHITE}")
        else:
            print(f"{Fore.RED}This move is invalid. Destination position is not empty.{Fore.WHITE}")
    else:
        print(f"{Fore.RED}This move is invalid. Starting position does not contain a knight.{Fore.WHITE}")

######################################################### test reset #########################################################
    game.reset_board()
    
    if str(game.board[7][4]) == '♔' :
        print(f"{Fore.GREEN}ok White King{Fore.WHITE}") # White King
    else :
        print(f"{Fore.RED}NOT OK {Fore.WHITE}")


    if str(game.board[0][1]) == '♞':
        print(f"{Fore.GREEN}ok Black knight{Fore.WHITE}")
    else :
        print(f"{Fore.RED}NOT OK {Fore.WHITE}") 
##################################################### test check #############################################################
    game.reset_board()
    game.make_move((6, 4), (4, 4))
    game.make_move((1, 3), (3, 3))
    game.make_move((6, 5), (3, 1))
    print(game.is_check("black"))
    if game.is_check("black") == True:
        print(f"{Fore.GREEN} check function is ok {Fore.WHITE}")
    else:
        print(f"{Fore.RED}NOT OK {Fore.WHITE}") 

###################################################### test rook ################################################################
    game.reset_board()
    game.make_move((6, 0), (4, 0))
    game.make_move((1, 0), (3, 0))
    game.make_move((7, 0), (5, 0))
    game.make_move((1, 1), (3, 1))
    game.make_move((5, 0), (5, 3))
    if str(game.board[5][3]) == '♖':
        if str(game.board[7][0]) == "None":
            print(f"{Fore.GREEN}This move is valid.{Fore.WHITE}")
        else:
            print(f"{Fore.RED}This move is invalid. Destination position is not empty.{Fore.WHITE}")
    else:
        print(f"{Fore.RED}This move is invalid. Starting position does not contain a knight.{Fore.WHITE}")



shoro=input("""
|///////////////////////////////////////|
|                                       |
|        Chess Game:                    |
|                                       |
|       A:[play]        t:[test]        |
|                                       |
|///////////////////////////////////////|
""")
if shoro=='a':

    game = ChessGame()
    game.play_game()
elif shoro=='t':
    test_chess_game()