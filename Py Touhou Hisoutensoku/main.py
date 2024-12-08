import pygame
from fighters import Twowho

pygame.init()

#code for defining the game window

W = 1000
H = 600

#The actual code to run the window
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Touhou (Not) Hisoutensoku') 

#loading the background(only puts the background in memory)

background = pygame.image.load('Assets/Stages/Shrine.png').convert_alpha()

#the actual function used to make the background appear

def loadbackground():
    scaled_background = pygame.transform.scale(background, (W, H))
    screen.blit(scaled_background, (0, 0)) #coordinate 0, 0 so the image is centered in the game window

#create instances of the fighters

fighter_1 = Twowho(200, 310)
fighter_2 = Twowho(700, 310)

#game loop

runtime = True #runtime is true to give the initial status of the display being opened

while runtime:

    loadbackground()

    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

#to update the background(basically make the background appear and make the function work)
    pygame.display.update()

pygame.quit() #to quit pygame cleanly after the loop is over