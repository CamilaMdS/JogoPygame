import pygame
from sys import exit
from pygame.locals import *
from random import randint
pygame.init()
start = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("jogo")
fundo = pygame.image.load("data/BG.png")
helice1 = pygame.image.load("data/fly1.png")
helice2 = pygame.image.load("data/fly2.png")
gameover = pygame.image.load("data/dead.png")
damage = pygame.image.load("data/Untitled-1.png")
bird1 = pygame.image.load("data/bird1.png")
bird2 = pygame.image.load("data/bird2.png")
x = 150
y = 375
altura = 100
largura = 250
velc = 8
boost = 15
switcher = True
updown = 0
up = False
down = False
frames = [helice1, gameover, damage]
z = 0
#musica
pygame.mixer.music.load("data/ambiente.mp3")
pygame.mixer.music.play(-1)
def imagepack ():
    colisao1 = bird1
    colisao2 = bird2
    global z
    start.blit(frames[z], (x, y))
    pygame.display.update()
    start.blit(fundo, (0, 0))
while switcher:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    movement = pygame.key.get_pressed()
    if movement[pygame.K_UP] and y > velc + 100:
        y -= velc
    if movement[pygame.K_DOWN] and y < 500 - 50 - velc:
        y += velc
    imagepack()




