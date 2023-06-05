import pygame
import sys
from back import Game

class Main:
    def __init__(self):
        pygame.init()
        self.background_image = pygame.image.load("src\TASVIRESTAN_18705312_t.jpg")
        self.screen = pygame.display.set_mode(self.background_image.get_size())
        pygame.display.set_caption("Chess Battle")
        self.back = Game()
        self.font = pygame.font.Font(None, 36)
      
    def mainloop(self):
        while True:
            self.screen.blit(self.background_image, (0, 0))  # Blit the background image 
            self.back.show_bg(self.screen)
            self.back.draw_navbar(self.screen)
            self.back.draw_pieces(self.screen)  # Moved draw_navbar to the back.py file
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if self.back.home_button_rect.collidepoint(pos):  # Update to self.back.home_button_rect
                            # Handle home button click
                            print("Home button clicked")
                        elif self.back.reset_button_rect.collidepoint(pos):  # Update to self.back.reset_button_rect
                            # Handle reset button click
                            print("Reset button clicked")
                        elif self.back.undo_button_rect.collidepoint(pos):  # Update to self.back.undo_button_rect
                            # Handle undo button click
                            print("Undo button clicked")

            pygame.display.update()



main = Main()
main.mainloop()
