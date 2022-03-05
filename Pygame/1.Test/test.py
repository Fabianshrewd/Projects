import pygame

#Start pygame
pygame.init()

#Make the screen
screen = pygame.display.set_mode((400, 300))
done = False

#Make an rectangle
pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

#Check if Pygame should be closed
while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True

    #Draw an rectangle
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

    #Update the window
    pygame.display.flip()
