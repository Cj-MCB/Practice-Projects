import pygame

pygame.init()
#Figure out how to change resolution to fit to screen later
screen = pygame.display.set_mode((1280, 720))
#The point of clock variable?
clock = pygame.time.Clock()
running = True

while running:
    # Area is for while pygame window is running (code will quit with pygame)
    #Quit when X is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Make a dark/light mode
    screen.fill("White")
    #Try to set title

    #Area for game code

    pygame.display.flip()

    #Limits FPS to 60
    clock.tick(60)

pygame.quit()