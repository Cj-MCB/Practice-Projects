import pygame
import os

pygame.init()
#Figure out how to change resolution to fit to screen later
resInfo = pygame.display.Info()
# fullscreen = pygame.display.set_mode((resInfo.current_w, resInfo.current_h))
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
fullscreen = pygame.FULLSCREEN
# screen = notfullscreen

#The point of clock variable?
clock = pygame.time.Clock()
running = True

while running:
    # Area is for while pygame window is running (code will quit with pygame)
    #Quit when X is pressed
    keypressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.FULLSCREEN:
            screen = pygame.display.set_mode((screenWidth, screenHeight), fullscreen)
        if keypressed[pygame.K_F11]:
            if fullscreen == True:
                ...
            elif fullscreen == False:
                ...
            screen = pygame.display.set_mode((screenWidth, screenHeight), fullscreen)

    #Make a dark/light mode
    # screen.fill("White")
    pygame.display.set_caption("SpamTheButton")
    titleIcon = pygame.image.load(os.path.join('Python', 'img', 'F.jpg')).convert()
    pygame.display.set_icon(titleIcon)

    #Area for game code

    pygame.display.flip()

    #Limits FPS to 60
    clock.tick(60)
    pygame.display.update()

pygame.quit()