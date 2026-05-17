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
    janela.set_title("Teste")
    #janela.set_background_color((0, 0, 255))
    
    niveis = {'facil': 0.5, "medio": 1, "dificil":1.5}
    intervalo_tiro = niveis[dificuldade]
    
    tiros = []
    inimigas = []
    nuvens_passadas =[]
    vel_tiro = 500 
    vel_inimiga = 150 # Aumentado para usar com dt
    
    shoot_sound = Sound("shoot.mp3")
    explosion_sound = Sound("explosion.mp3")
    time, time2 = 0 , 0
    time3 = 0 #a velocidade dos objetos de fundo
    intervalos_inimigas = 2 # Diminuído para 2 segundos para testar mais rápido
    tempo_passado = 0

    #score basico
    acertos = 0
    
    
    # Imagem nave
    nave = Sprite("spaceinvaders/images/nave.png")
    nave.set_position(jx/2 - nave.width/2, jy - nave.height)

    #nuvens
    nuvens = ["nuvens/nuvens(1).png", "nuvens/nuvens(2).png", "nuvens/nuvens(3).png", "nuvens/nuvens(4).png", "nuvens/nuvens(6).png"]

    while run:

        janela.set_background_color((4, 0, 255))
        dt = janela.delta_time()
        time += dt
        time2 += dt
        time3 += dt
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
            
        # Criando nuvens 
        if time3 >= 1:
            nuvem = Sprite(random.choice(nuvens))
            # Sorteio dinâmico para não nascerem no mesmo lugar
            nuvem.x = random.randint(0, int(jx - nuvem.width))
            nuvem.y = -nuvem.height
            nuvens_passadas.append(nuvem)
            time3 = 0

        for nuvem in nuvens_passadas:
            nuvem.y += 150 * dt#muda isso aqui depois, para parecer que apenas os avioes estão acelerando
            nuvem.draw()


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
        nuvens_passadas = [nuvem for nuvem in nuvens_passadas if nuvem.y<=jy]
        
        for n_inimiga in inimigas:
            if n_inimiga.y >= jy:
                os.system('clear')
                print("A nave conseguiu passar.\n Game Over")
                print("Naves abatidas: ", acertos)
                from gameover import game_over
                game_over(800, 600)


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
                from gameover import game_over
                game_over(800, 600)
        
        #aumentar a velocidade do inimigo conforme o tempo passa
        if tempo_passado > 2:
            vel_inimiga+=10
            tempo_passado=0


        nave.draw()
        janela.update()

jogar(800, 600, 'facil')
