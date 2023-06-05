
import os
class Piece:
    def __init__(self,name,color ,value,image=None,image_rect=None) -> None:
        self.name=name
        self.color=color
        self.moves=[]
        self.moved=False
        value_sign=1 if color =='white'else -1
        self.value=value+value_sign
        self.image=image
        self.image_rect=image_rect
        self.set_image()  # Call the set_image method to construct the image path
        print(f"Color: {self.color}")
        print(f"Name: {self.name}")
        print(f"Constructed Image Path: {self.image}")

    def set_image(self):
        self.image = os.path.join(f'F:/software_testing/img/{self.color} {self.name}.png')

    def add_moves(self,move):
        self.moves.append(move)


class Pawn(Piece):
    def __init__(self,  color) -> None:
        if color=='white':
            self.dir=-1
        else:
            self.dir=1
        super().__init__('pawn',color,1.0)

class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__('knight',color,3.0)

class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__('bishop',color,3.001)


class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__('rook',color,5.0)


class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__('queen',color,9.0)

class King(Piece):
    def __init__(self, color) -> None:
        super().__init__('king',color,1000.0)