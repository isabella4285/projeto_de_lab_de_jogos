from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *

def menu():
    run = True
    jx, jy = 800, 600

    janela = Window(jx, jy)
    janela.set_title("Menu")
    janela.set_background_color((0, 0, 0))

    # botoes
    #titulo = Sprite("botoes/titulo.png")
    b_jogar_low = Sprite("botoes/low/jogar_l.png")
    b_jogar_high = Sprite("botoes/high/jogar_h.png")
    b_dificuldade_low = Sprite("botoes/low/dificuldade_l.png")
    b_dificuldade_high = Sprite("botoes/high/dificuldade_h.png")
    b_ranking_low = Sprite("botoes/low/ranking_l.png")
    b_ranking_high = Sprite("botoes/high/ranking_h.png")
    b_sair_low = Sprite("botoes/low/sair_l.png")
    b_sair_high = Sprite("botoes/high/sair_h.png")

    def organizar():
        x_center = (janela.width - b_jogar_low.width) / 2
        b_jogar_low.set_position(x_center, 200)
        b_jogar_high.set_position(x_center, 200)

        x_center = (janela.width - b_dificuldade_low.width) / 2
        b_dificuldade_low.set_position(x_center, 300)
        b_dificuldade_high.set_position(x_center, 300)

        x_center = (janela.width - b_sair_low.width) / 2
        b_sair_low.set_position(x_center, 400)
        b_sair_high.set_position(x_center, 400)

        x_center = (janela.width - b_ranking_low.width) / 2
        b_ranking_low.set_position(x_center, 500)
        b_ranking_high.set_position(x_center, 500)

    organizar()

    mouse = Mouse()
    hovered_button = None

    while run:
        if mouse.is_over_object(b_jogar_low):
            hovered_button = "jogar"
            if mouse.is_button_pressed(1):
                from jogar import jogar
                jogar(jx, jy, 'facil')
        elif mouse.is_over_object(b_dificuldade_low):
            hovered_button = "dificuldade"
            if mouse.is_button_pressed(1):
                from dificuldade import dificuldade
                dificuldade(jx, jy)
        elif mouse.is_over_object(b_ranking_low):
            hovered_button = "ranking"
            if mouse.is_button_pressed(1):
                print("Ranking")
        elif mouse.is_over_object(b_sair_low):
            hovered_button = "sair"
            if mouse.is_button_pressed(1):
                run = False
        else:
            hovered_button = None

        if hovered_button == "jogar":
            b_jogar_high.draw()
        else:
            b_jogar_low.draw()

        if hovered_button == "dificuldade":
            b_dificuldade_high.draw()
        else:
            b_dificuldade_low.draw()

        if hovered_button == "ranking":
            b_ranking_high.draw()
        else:
            b_ranking_low.draw()

        if hovered_button == "sair":
            b_sair_high.draw()
        else:
            b_sair_low.draw()

        #titulo.draw()
        janela.update()

menu()

