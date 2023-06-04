import pygame

class Game:
    def __init__(self):
        pass
    def show_bg(self,surface):
        for row in range(8):
            for col in range(8):
                if (row + col)%2 ==0:
                    color = (234,235,200)
                else:
                    color= (119,154,88)
                rect=(col*(800//8),row *(800//8),(800//8),(800//8))
                pygame.draw.rect(surface,color,rect)
