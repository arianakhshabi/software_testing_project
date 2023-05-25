# test atumated text for about page with pygame
import pygame
pygame.init()
font=pygame.font.SysFont('arial', 30, bold=pygame.font.Font.bold)
screen = pygame.display.set_mode([800,500])

pygame.mixer.music.load("images\dramatic-guitar-140614.mp3")
pygame.mixer.music.play(-1)
timer=pygame.time.Clock()
message='Salam man baba haghiam'
snip = font.render('',True,'white')
counter=0
speed=3
done=False
run=True
while run:
    screen.fill('dark gray')
    timer.tick(60)
    pygame.draw.rect(screen,"black",[100,200,600,150])
    if counter< speed*len(message):
        counter+=1
    elif counter>= speed*len(message):
        done=True

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
    snip = font.render(message[0:counter//speed],True,'white')
    screen.blit(snip,(100,210))
    pygame.display.flip()
pygame.quit()