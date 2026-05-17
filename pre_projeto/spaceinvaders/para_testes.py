import pygame

imagem = "sair_l.png"
pygame.init()
tela = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Teste de Imagem")
imagem_carregada = pygame.image.load(imagem)
tela.blit(imagem_carregada, (100, 100))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

