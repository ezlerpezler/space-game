import pygame
from pygame.locals import *

walk_cycle = [pygame.image.load("sprites/adventurer-run-00.png"),
              pygame.image.load("sprites/adventurer-run-01.png"),
              pygame.image.load("sprites/adventurer-run-02.png"),
              pygame.image.load("sprites/adventurer-run-03.png"),
                  pygame.image.load("sprites/adventurer-run-04.png")]

idle_cycle = [pygame.image.load("sprites/adventurer-idle-00.png"),
              pygame.image.load("sprites/adventurer-idle-01.png"),
              pygame.image.load("sprites/adventurer-idle-02.png"),
              pygame.image.load("sprites/adventurer-idle-03.png")]

attack_cycle = [pygame.image.load("sprites/adventurer-attack2-02.png"),
              pygame.image.load("sprites/adventurer-attack2-03.png"),
              pygame.image.load("sprites/adventurer-attack2-04.png"),]

# Set up the slime animation
walk_slime_cycle = [pygame.image.load("slime/slime-move-0.png"),
              pygame.image.load("slime/slime-move-1.png"),
              pygame.image.load("slime/slime-move-2.png"),
              pygame.image.load("slime/slime-move-3.png")]

idle_slime_cycle = [pygame.image.load("slime/slime-idle-0.png"),
              pygame.image.load("slime/slime-idle-1.png"),
              pygame.image.load("slime/slime-idle-2.png"),
              pygame.image.load("slime/slime-idle-3.png")]