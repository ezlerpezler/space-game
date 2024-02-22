import pygame
from pygame.locals import *
from images import *
from random import randint



class Tree(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.imagesize = (200, 200)
        self.rawimage = pygame.image.load('tree.png').convert_alpha()
        self.image = pygame.transform.scale(self.rawimage, self.imagesize)
        self.rect = self.image.get_rect(topleft = pos)

class Slime(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)
        randint
        random_x = randint(500,2500)
        random_y = randint(0,1750)
        
        dead = False
        
        self.pos = (random_x,random_y)
        self.image = pygame.image.load('graphics/slime.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = self.pos)
        self.slimehealth = 0
        self.alive = True
        self.steps = 1
        
        self.bounderies = ((random_x - 20),(random_x + 20), (random_y - 20), (random_y + 20))
        self.speed = 3
        self.direction = pygame.math.Vector2()
        self.count = 0

    def update(self):
        
        while self.bounderies[0] < self.rect.x > self.bounderies[1] and self.bounderies[2] < self.rect.y > self.bounderies[3]:
            print ('help')
            if self.count == 20:
               self.steps = randint(2,8)
               self.direction.x = randint(-1,1)
               self.direction.y = randint(-1,1)
               self.count = 0
            else:
                self.count += 1
        self.rect.center += self.direction * self.steps 
        

# In your game loop or update function:
  # Update the player sprite
        
        
# 
#     def move(self,count):
#         
#         direc1 = randint(-5,5)
#         direc2 = randint(-5,5)
#         self.direction.x = direc1
#         self.direction.y = direc2
#         self.count = 0
# 
#             
#         self.rect.center += self.direction * self.speed

    
    def attack(self,slimehealth,points,player):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.state = 'attack'
            if self.slimehealth < 30:
                self.slimehealth += 1
            else:
                while self.alive == True:
                    self.kill()
                    self.alive = False
                    player.getpoints(points)
       
    
    def colly(self,player,slimehealth,points):
        if player.rect.colliderect(self.rect):
            self.attack(slimehealth,points,player)
                   
        

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.points = 0
        self.walk_cycle = walk_cycle
        self.idle_cycle = idle_cycle
        self.attack_cycle = attack_cycle
        self.state = 'idle'
        self.current_frame = 0
        self.animation_speed = 0.12
        self.animation_speed2 = 0.19
        self.image = self.idle_cycle[self.current_frame]
        self.rect = self.image.get_rect(center = pos)
        

    def input(self):
        keys = pygame.key.get_pressed()
        
        
#         else:
#             self.state = 'idle'
#             self.direction.y = 0    
#             
#         if keys[pygame.K_w]:
#             self.state = 'run'
#             self.direction.y = -1
# #         elif keys[pygame.K_s]:
# #             self.state = 'run'
# #             self.direction.y = 1
#         else:
#             self.state = 'idle'
#             self.direction.y = 0

        if keys[pygame.K_d]:
            self.state = 'run'
            self.direction.x = 1
        elif keys [pygame.K_r]:
            self.state = 'attack'
            self.direction.x = 0
        elif keys[pygame.K_a]:
            self.state = 'run'            
            self.direction.x = -1
        elif keys[pygame.K_s]:
            self.state = 'run'
            self.direction.y = 1
        elif keys[pygame.K_w]:
            self.state = 'run'
            self.direction.y = -1
        else:
            self.state = 'idle'
            self.direction.x = 0
            self.direction.y = 0
        
        
           
    def getpoints(self, points):
        self.points += 10
        print(self.points)
        
       
    def update(self):
        
        self.input()
        
        if self.state == 'attack':
            self.current_frame += self.animation_speed2
            if self.current_frame >= len(self.attack_cycle):
                self.current_frame = 0
            self.image = self.attack_cycle[int(self.current_frame)]
       
        elif self.state == 'run':
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.walk_cycle):
                self.current_frame = 0
            self.image = self.walk_cycle[int(self.current_frame)]
       
        else:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.idle_cycle):
                self.current_frame = 0
            self.image = self.idle_cycle[int(self.current_frame)]
  
        
        self.rect.center += self.direction * self.speed

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # box setup
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)

        # ground
        self.ground_surf = pygame.image.load('map4.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

        # camera speed
        self.keyboard_speed = 5
        self.mouse_speed = 0.2

        # zoom
        self.zoom_scale = 1
        self.internal_surf_size = (2500,2500)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

#     def zoom_keyboard_control(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_q]:
#             self.zoom_scale += 0.1
#         if keys[pygame.K_e]:
#             self.zoom_scale -= 0.1

    def custom_draw(self,player):
       
        self.center_target_camera(player)

#         self.zoom_keyboard_control()

        self.internal_surf.fill('#71ddee')

        # ground
        ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.ground_surf,ground_offset)

        # active elements
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surf.blit(sprite.image,offset_pos)

        scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_h))

        self.display_surface.blit(scaled_surf,scaled_rect)
