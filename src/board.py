from squre import Squre
from piece import *
class Board:
    def __init__(self) -> None:
       self.squres=[[0,0,0,0,0,0,0,0]for i in range(8)]

       self._create()
       self._add_piece('white')
       self._add_piece('black')
       
    def _create(self):

        for row in range(8):
            for col in range(8):
                self.squres[row][col]=Squre(row,col)

    def _add_piece(self,color):
        if color=='white':
            row_pawn,row_other=(6,7)
        else:
            row_pawn,row_other=(1,0)

   
        for col in range(8):
            self.squres[row_pawn][col]=Squre(row_pawn,col,Pawn(color))
        #knight
        self.squres[row_other][1]=Squre(row_other,1,Knight(color))
        self.squres[row_other][6]=Squre(row_other,6,Knight(color))
        #bishop
        self.squres[row_other][2]=Squre(row_other,2,Bishop(color))
        self.squres[row_other][5]=Squre(row_other,5,Bishop(color))
        #rook
        self.squres[row_other][0]=Squre(row_other,0,Rook(color))
        self.squres[row_other][7]=Squre(row_other,7,Rook(color))
        #queen
        self.squres[row_other][3]=Squre(row_other,3,Queen(color))
        #king
        self.squres[row_other][4]=Squre(row_other,4,King(color))

        
