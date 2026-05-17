from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
import random
from PPlay.sound import *
from PPlay.collision import *
import os

def jogar(jx, jy, dificuldade):
    run = True
    janela = Window(jx, jy)
    janela.set_title("Space Invaders")
    janela.set_background_color((0, 0, 0))
    
    niveis = {'facil': 0.5, "medio": 1, "dificil":1.5}
    intervalo_tiro = niveis[dificuldade]
    
    tiros = []
    inimigas = []
    vel_tiro = 500 
    vel_inimiga = 150 # Aumentado para usar com dt
    
    shoot_sound = Sound("shoot.mp3")
    explosion_sound = Sound("explosion.mp3")
    time, time2 = 0 , 0
    intervalos_inimigas = 2 # Diminuído para 2 segundos para testar mais rápido
    tempo_passado = 0

    #score basico
    acertos = 0
    abatido = False
    
    # Imagem nave
    nave = Sprite("spaceinvaders/images/nave.png")
    nave.set_position(jx/2 - nave.width/2, jy - nave.height)

    while run:
        janela.set_background_color((0, 0, 0))
        dt = janela.delta_time()
        time += dt
        time2 += dt
        tempo_passado += dt
        
        keyboard = janela.get_keyboard()
        if keyboard.key_pressed("ESC"):
            from menu import menu
            menu()
            run = False
        '''if acertos == 5:
            print("Aviões derrubados: ", acertos)
            run = False'''

        # Movimentação horizontal da nave
        if keyboard.key_pressed("LEFT"):
            if nave.x <= 0:
                nave.x = jx - nave.width # Ajustado para não brotar totalmente fora
            nave.x -= 300 * dt
        if keyboard.key_pressed("RIGHT"):
            if nave.x >= jx:
                nave.x = 0 
            nave.x += 300 * dt

        # Atirando    
        if keyboard.key_pressed("SPACE") and time >= intervalo_tiro:
            shoot_sound.play()
            novo_tiro = Sprite("spaceinvaders/images/nave_tiro.png")
            novo_tiro.x = nave.x + (nave.width/2) - (novo_tiro.width/2)
            novo_tiro.y = nave.y - novo_tiro.height
            tiros.append(novo_tiro)
            time = 0

        # Movimentando e desenhando tiros
        for tiro in tiros:
            tiro.y -= vel_tiro * dt
            tiro.draw()
            
        # Criando inimigos (Corrigido o >=)
        if time2 >= intervalos_inimigas:
            inimiga = Sprite("enemy.png")
            # Sorteio dinâmico para não nascerem no mesmo lugar
            inimiga.x = random.randint(0, int(jx - inimiga.width))
            inimiga.y = -inimiga.height
            inimigas.append(inimiga)
            time2 = 0

        # Movimentando e desenhando inimigos (Adicionado * dt)
        for n_inimiga in inimigas:
            n_inimiga.y += vel_inimiga * dt
            n_inimiga.draw()
            
        # Remoção segura de objetos fora da tela (List Comprehension) --nao

        tiros = [tiro for tiro in tiros if tiro.y >= -tiro.height]
        
        for n_inimiga in inimigas:
            if n_inimiga.y >= jy:
                os.system('clear')
                print("A nave conseguiu passar.\n Game Over")
                print("Naves abatidas: ", acertos)
                run = False



        '''
        for n_inimiga in inimigas:
                    n_inimiga.y += vel_inimiga
                    n_inimiga.draw()
                for n_inimiga in inimigas:
                    if n_inimiga.y==jy:      
                        inimigas.remove(n_inimiga)'''


        #detectando colisoes
        for tiro in tiros:
            for inimiga in inimigas:
                if Collision.collided(tiro, inimiga):
                    explosion_sound.play()
                    acertos += 1
                    tiros.remove(tiro)
                    inimigas.remove(inimiga)
        for inimiga in inimigas:
            if Collision.collided(inimiga, nave):
                run = False
                os.system('clear')
                print("NAVE ABATIDA!")
                print("Aviões derrubados: ", acertos)
        
        #aumentar a velocidade do inimigo conforme o tempo passa
        if tempo_passado > 2:
            vel_inimiga+=10
            tempo_passado=0


        nave.draw()
        janela.update()

jogar(800, 600, 'facil')
