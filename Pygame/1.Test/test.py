import pygame

#class
#Creature
class Creature():
    pos_x = int(0)
    pos_y = int(0)
    size_x = int(0)
    size_y = int(0)
    color = (50, 50, 50)

    #init
    def __init__(self, x, y, x2, y2, c):
        self.pos_x = x
        self.pos_y = y
        self.size_x = x2
        self.size_y = y2
        self.color = c

    #Movement by Command
    def movement_display(self, screen):
        Rectangle(screen, self.color, self.pos_x, self.pos_y, self.size_x, self.size_y)

    def movement_keys(self, key):
        if key == "w":
            self.pos_y -= 0.5
        if key == "s":
            self.pos_y += 0.5
        if key == "d":
            self.pos_x += 0.5
        if key == "a":
            self.pos_x -= 0.5

#functions
#function draw rectangle
def Rectangle(screen, color, pos_x, pos_y, size_x, size_y):
    pygame.draw.rect(screen, color, pygame.Rect(pos_x, pos_y, size_x, size_y))

#Main Program
#Start pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
clock = pygame.time.Clock()

#Create an player
player = Creature(100, 100, 100, 100, (30, 30, 30, 30))

#Check if Pygame should be closed
while not done:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
    
    #Loop
    #Refill the screen
    screen.fill((1, 0, 66))
    
    #Show the character and check for movement
    player.movement_display(screen)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        player.movement_keys("w")
    if pressed[pygame.K_s]:
        player.movement_keys("s")
    if pressed[pygame.K_a]:
        player.movement_keys("a")
    if pressed[pygame.K_d]:
        player.movement_keys("d")

    #Make a clock so it runs slower
    clock.tick(1000)

    #Update the window
    pygame.display.flip()
    pygame.event.pump()
