import pygame, sys
from random import randint
from class1703 import *
from images import *
from startup2 import *

Tree = Tree
Slime = Slime
Player = Player 
CameraGroup = CameraGroup
pos = 0

sequence = sequence


pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.event.set_grab(True)

# setup
game_state = "start"

colly = 0
camera_group = CameraGroup()
random_x = randint(1000,2000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
random_y = randint(1000,2000)
player = Player((640,360),camera_group)


slimehealth = 0
points = 0


color = (177, 209, 159)
black = (0,0,0)
font = pygame.font.SysFont("dubai",30)


slime1 = Slime(camera_group)
slime2 = Slime(camera_group)
slime3 = Slime(camera_group)
slime4 = Slime(camera_group)
slime5 = Slime(camera_group)
slime6 = Slime(camera_group)
slime7 = Slime(camera_group)
slime8 = Slime(camera_group)
slime9 = Slime(camera_group)
slime10 = Slime(camera_group)

slimelist = [slime1,slime2,slime3,slime4,slime5,slime6,slime7,slime8,slime9,slime10]


def slimeregen():
    for i in range(slimelist):
        slimelist[i] = Slime(camera_group)
    


for i in range(20):
    random_x = randint(500,2500)
    random_y = randint(0,1750)
    Tree((random_x,random_y),camera_group)

count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEWHEEL:
            camera_group.zoom_scale += event.y * 0.03

    if player.points == 100:
        game_state = "end"
        
    if game_state == "start":
        sequence()
        game_state = "game"
        
    if game_state == "game":
        
        slime1.colly(player,slimehealth,points)
        slime2.colly(player,slimehealth,points)
        slime3.colly(player,slimehealth,points)
        slime4.colly(player,slimehealth,points)
        slime5.colly(player,slimehealth,points)
        slime6.colly(player,slimehealth,points)
        slime7.colly(player,slimehealth,points)
        slime8.colly(player,slimehealth,points)
        slime9.colly(player,slimehealth,points)
        slime10.colly(player,slimehealth,points)
        
        slime1.update()
        slime2.update()
        slime3.update()
        slime4.update()
        slime5.update()
                
        screen.fill('#71ddee')
        
        camera_group.update()
        camera_group.custom_draw(player)
        
        pygame.draw.rect(screen, color, pygame.Rect(15, 20, 120, 30))

        score = font.render(str(player.points),True,black)
        score2 = font.render("score:",True,black)
        screen.blit(score2,(25,25))
        screen.blit(score,(100,25))
        
        pygame.display.update()
    clock.tick(60)
        
    if game_state == "end":
        end()
        
    
