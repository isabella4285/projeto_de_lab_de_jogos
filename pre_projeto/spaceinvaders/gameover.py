from PPlay.window import *
from PPlay.sprite import *
import random
from PPlay.sound import *


def game_over(jx, jy):
    run = True
    janela = Window(jx, jy)
    janela.set_title("Game Over")
    mensagem = Sprite("gameover.png")
    som = Sound("game_over.wav")
    play = True

    while run:

        janela.set_background_color((255, 255, 255))
        mensagem.set_position(jx/2-mensagem.width/2, jy/2-mensagem.height/2)
        if play:
            som.play()
            play = False
        mensagem.draw()
        janela.update()
