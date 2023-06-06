
import pygame
from board import Board


class Drag:
    def __init__(self) -> None:
        self.mouseX=0
        self.mouseY=0
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None
        self.dragging = False
        


    def update_blit(self, surface):
        # texture
        piece = self.piece
        # img
        img = pygame.image.load(piece.image)
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.image_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.piece.image_rect)


    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # (xcor, ycor)
    def save_initial(self, pos):
        self.initial_row = (pos[1]-75) // (800 // 8)
        self.initial_col = (pos[0]-50) // (800 // 8)

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False