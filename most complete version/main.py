import pygame
from fighters import Twowho

pygame.init()

#code for defining the game window

W = 1000
H = 600

#The actual code to run the window
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Touhou (Not) Hisoutensoku') 
clock = pygame.time.Clock()
FPS = 60

#define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#loading the background(only puts the background in memory)
background = pygame.image.load('Assets/Stages/Shrine.png').convert_alpha()

#sprites
'''twowho1_sprite_idle = [pygame.image.load('Assets/Sprites/idle/1.png'),
                       pygame.image.load('Assets/Sprites/idle/2.png'),
                       pygame.image.load('Assets/Sprites/idle/3.png'),
                       pygame.image.load('Assets/Sprites/idle/4.png'),
                       pygame.image.load('Assets/Sprites/idle/5.png'),
                       pygame.image.load('Assets/Sprites/idle/6.png'),
                       pygame.image.load('Assets/Sprites/idle/7.png'),
                       pygame.image.load('Assets/Sprites/idle/8.png'),
                       pygame.image.load('Assets/Sprites/idle/9.png'),
                       pygame.image.load('Assets/Sprites/idle/10.png'),
                       pygame.image.load('Assets/Sprites/idle/11.png')]

twowho1_sprite_walk_backwards = [pygame.image.load('Assets/Sprites/backwards/1.png'),
                       pygame.image.load('Assets/Sprites/backwards/2.png'),
                       pygame.image.load('Assets/Sprites/backwards/3.png'),
                       pygame.image.load('Assets/Sprites/backwards/4.png'),
                       pygame.image.load('Assets/Sprites/backwards/5.png'),
                       pygame.image.load('Assets/Sprites/backwards/6.png'),
                       pygame.image.load('Assets/Sprites/backwards/7.png'),
                       pygame.image.load('Assets/Sprites/backwards/8.png')]

twowho1_sprite_walk_forwards = [pygame.image.load('Assets/Sprites/Idle/1.png'),
                       pygame.image.load('Assets/Sprites/forwards/2.png'),
                       pygame.image.load('Assets/Sprites/forwards/3.png'),
                       pygame.image.load('Assets/Sprites/forwards/4.png'),
                       pygame.image.load('Assets/Sprites/forwards/5.png'),
                       pygame.image.load('Assets/Sprites/forwards/6.png'),
                       pygame.image.load('Assets/Sprites/forwards/7.png')]

twowho1_sprite_jump = [pygame.image.load('Assets/Sprites/jump/1.png'),
                       pygame.image.load('Assets/Sprites/jump/2.png'),
                       pygame.image.load('Assets/Sprites/jump/3.png'),
                       pygame.image.load('Assets/Sprites/jump/4.png'),
                       pygame.image.load('Assets/Sprites/jump/5.png'),
                       pygame.image.load('Assets/Sprites/jump/6.png'),
                       pygame.image.load('Assets/Sprites/jump/7.png'),
                       pygame.image.load('Assets/Sprites/jump/8.png'),
                       pygame.image.load('Assets/Sprites/jump/9.png')]

twowho1_sprite_hit = [pygame.image.load('Assets/Sprites/hit/1.png'),
                       pygame.image.load('Assets/Sprites/hit/2.png'),
                       pygame.image.load('Assets/Sprites/hit/3.png')]

twowho1_sprite_attack1 = [pygame.image.load('Assets/Sprites/attack1/1.png'),
                       pygame.image.load('Assets/Sprites/attack1/2.png'),
                       pygame.image.load('Assets/Sprites/attack1/3.png'),
                       pygame.image.load('Assets/Sprites/attack1/4.png'),
                       pygame.image.load('Assets/Sprites/attack1/5.png'),
                       pygame.image.load('Assets/Sprites/attack1/6.png'),
                       pygame.image.load('Assets/Sprites/attack1/7.png')]

twowho1_sprite_attack2 = [pygame.image.load('Assets/Sprites/attack2/1.png'),
                       pygame.image.load('Assets/Sprites/attack2/2.png'),
                       pygame.image.load('Assets/Sprites/attack2/3.png'),
                       pygame.image.load('Assets/Sprites/attack2/4.png'),
                       pygame.image.load('Assets/Sprites/attack2/5.png')]'''

#the actual function used to make the background appear
def loadbackground():
    scaled_background = pygame.transform.scale(background, (W, H))
    screen.blit(scaled_background, (0, 0)) #coordinate 0, 0 so the image is centered in the game window

#function for health bar
def draw_health_bar(health, x, y):
    ratio = health/ 100
    pygame.draw.rect(screen, WHITE, (x-2, y-2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400*ratio, 30))

#instances of fighters
fighter_1 = Twowho(1, 200, 310)
fighter_2 = Twowho(2, 700, 310)

#game loop

runtime = True #runtime is true to give the initial status of the display being opened

while runtime:

    clock.tick(FPS) 

    loadbackground()

    #show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #move fighters
    fighter_1.controls(W, H, screen, fighter_2)
    fighter_2.controls(W, H, screen, fighter_1)

    #draw the fighters on screen
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

#to update the background(basically make the background appear and make the function work)
    pygame.display.update()

pygame.quit() #to quit pygame cleanly after the loop is over