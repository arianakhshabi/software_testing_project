import pygame
from board import Board

class Game:
    def __init__(self):
        self.home_button_rect = pygame.Rect(10, 10, 100, 30)
        self.reset_button_rect = pygame.Rect(120, 10, 100, 30)
        self.undo_button_rect = pygame.Rect(230, 10, 100, 30)
        self.board = Board()

    def show_bg(self, surface):
        surface_width = surface.get_width()
        surface_height = surface.get_height()

        background_image = pygame.image.load("src/TASVIRESTAN_18705312_t.jpg")  # Replace "background.jpg" with your actual image file
        background_image = pygame.transform.scale(background_image, (surface_width, surface_height))
        surface.blit(background_image, (0, 0))

        chessboard_size = 800
        chessboard_x = (surface_width - chessboard_size) // 2
        chessboard_y = (surface_height - chessboard_size - 50) // 2  # Subtract 50 for the height of the navbar
        chessboard_rect = pygame.Rect(chessboard_x, chessboard_y, chessboard_size, chessboard_size)

        pygame.draw.rect(surface, (234, 235, 200), chessboard_rect)

        square_size = chessboard_size // 8
        for row in range(8):
            for col in range(8):
                square_x = chessboard_x + col * square_size
                square_y = chessboard_y + row * square_size   # Increased y-coordinate to account for the navbar

                if (row + col) % 2 == 0:
                    color = (200, 244, 249)
                else:
                    color = (24, 222, 149)

                square_rect = pygame.Rect(square_x, square_y, square_size, square_size)
                pygame.draw.rect(surface, color, square_rect)
    
    def draw_pieces(self, surface):
        for row in range(8):
            for col in range(8):
                if self.board.squres[row][col].has_piece():
                    piece = self.board.squres[row][col].piece

                    img = pygame.image.load(piece.image)  # Load and convert the image
                    img = pygame.transform.scale(img, (80, 80))  # Scale the image to the desired size

                    img_center = col * (800 // 8) + (800 // 8) // 2 + 75, row * (800 // 8) + (800 // 8) // 2 + 50  # Add the desired offset
                    piece.image_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.image_rect)


    def draw_navbar(self, surface):
        surface_width = surface.get_width()

        navbar_height = 50
        navbar_color = (0, 0, 0)
        navbar_rect = pygame.Rect(0, 0, surface_width, navbar_height)

        pygame.draw.rect(surface, navbar_color, navbar_rect)

        button_width = 100
        button_height = 30
        button_spacing = 20
        total_buttons_width = 3 * button_width + 2 * button_spacing
        start_x = (surface_width - total_buttons_width) // 2

        self.home_button_rect = pygame.Rect(start_x, 10, button_width, button_height)
        self.reset_button_rect = pygame.Rect(start_x + button_width + button_spacing, 10, button_width, button_height)
        self.undo_button_rect = pygame.Rect(start_x + 2 * (button_width + button_spacing), 10, button_width, button_height)

        button_color = (255, 255, 255)
        button_text_color = (0, 0, 0)
        font = pygame.font.Font(None, 24)

        pygame.draw.rect(surface, button_color, self.home_button_rect)
        pygame.draw.rect(surface, button_color, self.reset_button_rect)
        pygame.draw.rect(surface, button_color, self.undo_button_rect)

        home_button_text = font.render("Home", True, button_text_color)
        reset_button_text = font.render("Reset", True, button_text_color)
        undo_button_text = font.render("Undo", True, button_text_color)

        home_button_text_pos = home_button_text.get_rect(center=self.home_button_rect.center)
        reset_button_text_pos = reset_button_text.get_rect(center=self.reset_button_rect.center)
        undo_button_text_pos = undo_button_text.get_rect(center=self.undo_button_rect.center)

        surface.blit(home_button_text, home_button_text_pos)
        surface.blit(reset_button_text, reset_button_text_pos)
        surface.blit(undo_button_text, undo_button_text_pos)
