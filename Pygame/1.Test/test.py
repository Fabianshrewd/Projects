import pygame

#classe
#enemie
class Creature:
    pos_x = int(0)
    pos_y = int(0)

#functions
#function draw rectangle
def Rectangle(screen, color, pos_x, pos_y, size_x, size_y):
    pygame.draw.rect(screen, color, pygame.Rect(pos_x, pos_y, size_x, size_y))

#function for the collider
def Collider():
    x = 1

#Main Program
#Start pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
clock = pygame.time.Clock()
movement_x = int(10)
movement_y = int(10)

#Check if Pygame should be closed
while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
    
    #Loop
    #Refill the screen
    screen.fill((1, 0, 66))
    
    #Build a border
    color_black = (0, 0 , 0)
    Rectangle(screen, color_black, 0, 0, 1280, 10)
    Rectangle(screen, color_black, 0, 0, 10, 720)
    Rectangle(screen, color_black, 0, 710, 1280, 10)
    Rectangle(screen, color_black, 1270, 0, 10, 720)
    
    #Collider
    

    #Draw an rectangle
    color = (0, 128, 255)
    Rectangle(screen, color, movement_x, movement_y, 100, 100)
    
    #Movement on Key
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        if movement_x < 1170:
            movement_x += 1
    if pressed[pygame.K_a]: 
        if movement_x > 10:
            movement_x -= 1
    if pressed[pygame.K_s]: 
        if movement_y < 610:
            movement_y += 1
    if pressed[pygame.K_w]: 
        if movement_y > 10:
            movement_y -= 1

    #Make a clock so it runs slower
    clock.tick(1000)

    #Update the window
    pygame.display.flip()
