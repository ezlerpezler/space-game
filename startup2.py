import pygame
pygame.init()

screen = pygame.display.set_mode((1280,720))

main_music = pygame.mixer.Sound("music.mp3")

def end():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Boo', 30)
    title = font.render('CONGRATUALTIONS, YOU HAVE COMPLETED THE GAME. PRESS ESC TO EXIT', True, (255, 255, 255))
    screen.blit(title, title.get_rect(center = screen.get_rect().center))
    pygame.display.update()
    
def message(text):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Boo', 30)
    font1 = pygame.font.SysFont('arial', 20)
    title = font.render(text, True, (255, 255, 255))
    screen.blit(title, title.get_rect(center = screen.get_rect().center))
    pygame.display.update()
    

def sequence():
    pygame.mixer.music.load('tv_glitch.mp3')
    pygame.mixer.music.play(3)

    
    message('INCOMING TRANSMISSION')
    pygame.time.delay(500)
    message(' ')
    pygame.time.delay(500)
    message('INCOMING TRANSMISSION')
    pygame.time.delay(500)
    message('')
    pygame.time.delay(500)
    message('INCOMING TRANSMISSION')
    pygame.time.delay(350)
    message('')
    pygame.time.delay(500)
    message('WARNING: CONNECTION UNSTABLE')
    pygame.time.delay(350)
    message('')
    pygame.time.delay(500)
    message('INCOMING TRANSMISSION')
    pygame.time.delay(350)
    message('')
    pygame.time.delay(700)
    message('WARNING: CONNECTION UNSTABLE')
    pygame.time.delay(700)
    message('H..HH-L-O.. CO-MM--NDR. COMANDER! DO Y--U -ERE ME?')
    pygame.time.delay(3000)
    message('WE-----RE LO-O--S--NG Y-U. YO--U RE--AD? HELLO?')
    pygame.time.delay(3000)
    pygame.mixer.Sound.play(main_music)
    message('S--ORR-Y ')
    pygame.time.delay(3000)
    pygame.mixer.music.stop()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    message('PLANET 65798')
    pygame.time.delay(3000)
    message('OBJECTIVE: KILL ALL SLIMES')
    pygame.time.delay(3000)
    message('MOVE: WASD')
    pygame.time.delay(3000)
    message('ATTACK: R')
    pygame.time.delay(3000)
    message('GOOD LUCK')
    pygame.time.delay(3000)
    
    
