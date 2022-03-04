import pygame

#Start pygame
pygame.init()

#Make the screen
screen = pygame.display.set_mode((400, 300))
done = False

#Check if Pygame should be closed
while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True

#Update the window
pygame.display.flip()
