

from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
import pygame
#corrigir o uso do delta time e as velocidades

em_jogo = True

wx, wy = 1000, 700
pontos = [0, 0] #jogador, ia
#modificar a contagem de pontos
janela = Window(wx, wy)
janela.set_title("ping pong")

janela.set_background_color((40, 40, 40))
bola=Sprite("bola.png")
bola.image = pygame.transform.scale(bola.image, (40, 40))

barra1 = Sprite("barra.png")
barra1.image = pygame.transform.scale(barra1.image, (30, 100))

barra2 = Sprite("barra.png")
barra2.image = pygame.transform.scale(barra2.image, (30, 100))
barra1.set_position(0, wy/2-barra1.height/2)
barra2.set_position(wx-30, wy/2-barra1.height/2)

bola.x = (janela.width)/2 - (bola.width)/2
bola.y = (janela.height)/2 - (bola.height)/2
x, y = 150, 150
velx, vely = x, y
print(bola.width, bola.height)
bola.width, bola.height = bola.image.get_width(), bola.image.get_height()
while True:
    janela.set_background_color((100, 0, 90))

    if em_jogo:
        bola.x += velx*janela.delta_time()
        bola.y += vely*janela.delta_time()
    else: #espera espaco para resetar
        if janela.get_keyboard().key_pressed("space"):
            bola.set_position((wx)/2-bola.width/2, (wy)/2-bola.height/2)
            barra1.set_position(0, wy/2-barra1.height/2)
            velx, vely = x, y
            em_jogo = True
    #verificar pontos depois q a bola sai da tela
    if bola.x > wx: #direita-> ponto do jogador
        pontos[0] += 1
        print(pontos)
        em_jogo = False
        bola.set_position((wx)/2-bola.width/2, (wy)/2-bola.height/2)
        barra1.set_position(0, wy/2-bola.height/2)

    elif bola.x < -bola.width:
        pontos[1] += 1
        print(pontos)
        em_jogo = False
        bola.set_position((wx)/2-bola.width/2, (wy)/2-barra1.height/2)
        barra1.set_position(0, wy/2-barra1.height/2)
        
    
    #desenhar tudo
    bola.draw()
    barra1.draw()
    barra2.draw()

    #colisoes com margens horizontais
    if bola.y <= 0 or bola.y >= wy - bola.height:
        vely *= -1
    
    #movendo a barra a esquerda
    key_pressed = janela.get_keyboard()
    if key_pressed.key_pressed("UP") and barra1.y>barra1.width-bola.height:
        barra1.y = barra1.y - ((y)*janela.delta_time())
    if key_pressed.key_pressed("DOWN") and barra1.y<wy-barra1.height/2-bola.height/2:
        barra1.y = barra1.y + (y*janela.delta_time())
    
    #movendo a barra direita
    if bola.y>barra2.width-bola.height and bola.y<(wy-barra2.height/2)-bola.height/2:
        barra2.y = bola.y #1*janela.delta_time

    #adicionando colisao
    colisao_direita = Collision.collided(bola, barra2)
    if colisao_direita:
        #print("colidiu b2")
        velx *=-1
    
    colisao_esquerda = Collision.collided(bola, barra1)
    if colisao_esquerda:
        #print("colidiu b1")
        velx *=-1

    
    janela.update()
    


        

