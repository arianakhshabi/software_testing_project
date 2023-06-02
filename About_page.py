import pygame
import os

pygame.init()

font = pygame.font.SysFont('Amelaryas', 32, bold=pygame.font.Font.bold)
screen = pygame.display.set_mode([1024, 1024])
pygame.display.set_caption("Scrolling Text")

bg = pygame.image.load('images/934cd7b4-c97b-4764-9796-058cb1eecce9.jpg')

pygame.mixer.music.load("images/dramatic-guitar-140614.mp3")
pygame.mixer.music.play(-1)
timer = pygame.time.Clock()
message = 'this game \nwas written by Arian Akhshabi \nfor software testing final project\nSTID:990201110009'

scroll_speed = 3
counter = 0

done = False
run = True
while run:
    screen.blit(bg, (0, 0))
    timer.tick(60)

    if counter < len(message) * scroll_speed:
        counter += 1
    elif counter >= len(message) * scroll_speed:
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    pygame.quit()  # Close the current window
                    os.system("python fist_page_game.py")  # Open first_game_page.py
                    run = False

    rendered_lines = []
    current_line = ""
    for char_index in range(counter // scroll_speed):
        if message[char_index] != '\n':
            current_line += message[char_index]
        else:
            rendered_lines.append(current_line)
            current_line = ""

    rendered_lines.append(current_line)  # Add the last line

    y_offset = 400
    for line in rendered_lines:
        line_surface = font.render(line, True, 'Black')
        screen.blit(line_surface, (270, y_offset))
        y_offset += line_surface.get_height() + 5  # Add some spacing between lines

    # Draw back button
    back_button = font.render("Back", True, 'Black')
    back_button_rect = back_button.get_rect(center=((screen.get_width() // 2)-40, y_offset + 100))
    screen.blit(back_button, back_button_rect)

    pygame.display.flip()

pygame.quit()
