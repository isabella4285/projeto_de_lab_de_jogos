from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
import random
from PPlay.sound import *

def jogar(jx, jy, dificuldade):
    run = True
    janela = Window(jx, jy)
    janela.set_title("Space Invaders")
    janela.set_background_color((0, 0, 0))
    niveis = {'facil': 0.5, "medio": 1, "dificil":1.5}
    intervalo_tiro = niveis[dificuldade]
    tiros = []
    inimigas = []
    vel_tiro = 500 #usando dt
    shoot_sound = Sound("shoot.mp3")
    time = 0 
    intervalos_inimigas = 0
    vel_inimiga = 1
    #adicionar deltatime
    
    #imagem nave
    nave = Sprite("spaceinvaders/images/nave.png")
    nave.set_position(jx/2-nave.width/2, jy-nave.height)

    pos = random.randint(int(nave.width), jx)
    #inimiga = Sprite("enemy.png")
    #inimiga.set_position(pos, 0)

    while True:
        janela.set_background_color((0, 0, 0))
        dt = janela.delta_time()
        time += dt
        intervalos_inimigas += dt
        keyboard = janela.get_keyboard()
        if keyboard.key_pressed("ESC"):
            from menu import menu
            menu()
            run = False
    
        #movimentacao horizontal da nave
        if keyboard.key_pressed("LEFT"):
            if nave.x<=0:
                nave.x = jx 
            nave.x-=300*dt
        if keyboard.key_pressed("RIGHT"):
            if nave.x>=jx:
                nave.x=0 
            nave.x+=300*dt

        #atirando    
        if keyboard.key_pressed("SPACE") and time>=intervalo_tiro:
                print("tiro")
                shoot_sound.play()
                novo_tiro = Sprite("spaceinvaders/images/nave_tiro.png")
                novo_tiro.x = nave.x+(nave.width/2) - (novo_tiro.width/2)
                novo_tiro.y = nave.y - novo_tiro.height
                #tiros.append(nave_tiro)
                tiros.append(novo_tiro)
                print(len(tiros))
                time = 0

        for tiro in tiros:
            tiro.y -= vel_tiro*dt
            tiro.draw()
        for tiro in tiros:
            if tiro.y<-tiro.height:
                tiros.remove(tiro)

        #animando inimigo
        if intervalos_inimigas == 50:
            inimiga = Sprite("enemy.png")
            #inimiga.set_position(pos, 0)
            inimiga.x = pos
            inimiga.y = 0
            #inimiga.draw()
            inimigas.append(inimiga)
            intervalos_inimigas = 0
        for n_inimiga in inimigas:
            n_inimiga.y += vel_inimiga
            n_inimiga.draw()
        for n_inimiga in inimigas:
            if n_inimiga.y>jy:      
                inimigas.remove(n_inimiga)

        nave.draw()
        
        janela.update()

jogar(800, 600, 'facil')








    