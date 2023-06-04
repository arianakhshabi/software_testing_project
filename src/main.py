import pygame 
import sys
from back import Game
class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen= pygame.display.set_mode((800,800))
        pygame.display.set_caption("Chess Battle")
        self.back= Game()
    def mainloop(self):
        while True:
            self.back.show_bg(self.screen)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

                     
            pygame.display.update()



main=Main()
main.mainloop()