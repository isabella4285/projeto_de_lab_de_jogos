from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *

def dificuldade(jx, jy):
    janela = Window(jx, jy)
    janela.set_title("Dificuldade")
    janela.set_background_color((0, 0, 0))

    #botoes
    b_facil_low = Sprite("botoes/dificuldade/facill.png")
    b_facil_high = Sprite("botoes/dificuldade/facilh.png")
    b_medio_low = Sprite("botoes/dificuldade/mediol.png")
    b_medio_high = Sprite("botoes/dificuldade/medioh.png")
    b_dificil_low = Sprite("botoes/dificuldade/dificill.png")
    b_dificil_high = Sprite("botoes/dificuldade/dificulh.png")
    #titulo = Sprite("botoes/dificuldade/titulodificuldade.png")
    run=True
    #titulo.x = (janela.width - titulo.width) / 2
    b_facil_low.x = (janela.width - b_facil_low.width) / 2
    b_facil_low.y = 200
    b_facil_high.set_position(b_facil_low.x, b_facil_low.y)

    b_medio_low.x = (janela.width - b_medio_low.width) / 2
    b_medio_low.y = 300
    b_medio_high.set_position(b_medio_low.x, b_medio_low.y)

    b_dificil_low.x = (janela.width - b_dificil_low.width) / 2
    b_dificil_low.y = 400
    b_dificil_high.set_position(b_dificil_low.x, b_dificil_low.y)

    mouse = Mouse()
    hovered_button = None

    while run:
        keyboard = janela.get_keyboard()
        if keyboard.key_pressed("ESC"):
            from menu import menu
            menu()
            run = False
        if mouse.is_over_object(b_facil_low):
            hovered_button = "facil" 
            if mouse.is_button_pressed(1):
                print("Dificuldade: Fácil")
                from jogar import jogar
                jogar(800, 600, 'facil')

        elif mouse.is_over_object(b_medio_low):
            hovered_button = "medio"
            if mouse.is_button_pressed(1):
                print("Dificuldade: Médio")
                from jogar import jogar
                jogar(800, 600, 'medio')

        elif mouse.is_over_object(b_dificil_low):
            hovered_button = "dificil"
            if mouse.is_button_pressed(1):
                print("Dificuldade: Difícil")
                from jogar import jogar
                jogar(800, 600, 'dificil')
        else:
            hovered_button = None

        if hovered_button == "facil":
            b_facil_high.draw()
        else:
            b_facil_low.draw()
        if hovered_button == "medio":
            b_medio_high.draw()
        else:
            b_medio_low.draw()
        if hovered_button == "dificil":
            b_dificil_high.draw()
        else:
            b_dificil_low.draw()
        
        #titulo.draw()
        janela.update()
dificuldade(800, 600)