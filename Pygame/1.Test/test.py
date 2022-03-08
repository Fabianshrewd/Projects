import pygame

#class
#Creature
class Creature():
    pos_x = int(0)
    pos_y = int(0)
    size_x = int(0)
    size_y = int(0)
    rect_stats = pygame.Rect(pos_x, pos_y, size_x, size_y)
    color = (50, 50, 50)

    #init
    def __init__(self, x, y, x2, y2, c):
        self.pos_x = x
        self.pos_y = y
        self.size_x = x2
        self.size_y = y2
        self.color = c

    #Update the Rect
    def updateRect(self):
        self.rect_stats = pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)

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

#Collider
def collider_object_x(object1, object2, axes):
    object1.x += axes
    if pygame.Rect.colliderect(object1, object2):
        return False
    else:
        return True

def collider_object_y(object1, object2, axes):
    object1.y += axes
    if pygame.Rect.colliderect(object1, object2):
        return False
    else:
        return True

#Main Program
#Start pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
clock = pygame.time.Clock()

#Create an player
player = Creature(100, 100, 100, 100, (20, 20, 20))
player2 = Creature(300, 300, 100, 100, (30, 30, 30))

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
    player2.movement_display(screen)
   
    #Build the Rect for the collider
    player.updateRect()
    player2.updateRect()
    
    #Check which buttons are pressed
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and collider_object_y(player.rect_stats, player2.rect_stats, -1):
        player.movement_keys("w")
    if pressed[pygame.K_s] and collider_object_y(player.rect_stats, player2.rect_stats, 1):
        player.movement_keys("s")
    if pressed[pygame.K_a] and collider_object_x(player.rect_stats, player2.rect_stats, -1):
        player.movement_keys("a")
    if pressed[pygame.K_d] and collider_object_x(player.rect_stats, player2.rect_stats, 1):
        player.movement_keys("d")
    
    if pressed[pygame.K_i] and collider_object_y(player.rect_stats, player2.rect_stats, 1):
        player2.movement_keys("w")
    if pressed[pygame.K_k] and collider_object_y(player.rect_stats, player2.rect_stats, -1):
        player2.movement_keys("s")
    if pressed[pygame.K_j] and collider_object_x(player.rect_stats, player2.rect_stats, 1):
        player2.movement_keys("a")
    if pressed[pygame.K_l] and collider_object_x(player.rect_stats, player2.rect_stats, -1):
        player2.movement_keys("d")

    #Make a clock so it runs slower
    clock.tick(1000)

    #Update the window
    pygame.display.flip()
    pygame.event.pump()
