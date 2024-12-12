
import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()

# Define a altura e largura da janela
screen_width = 720
screen_height = 480
tela = pygame.display.set_mode((screen_height,screen_width)) #define a proporção da janela
pygame.display.set_caption('Jogo da cobrinha') # muda o nome da janela
cor = [0,0,0] #Define a cor de fundo da janela

class jogador:
    def __init__(self,player_x,player_y,player_color,player_largura,player_altura):
        self.player_x = player_x
        self.player_y = player_y
        self.player_color = player_color
        self.player_largura = player_largura
        self.player_altura = player_altura

localmusica = "C:\\Users\\teste\\Documents\\Desinvilvimento\\Projetos-em-python\\jogo_da_cobrinha\\virtual\\Scripts\\sons\\doom.mp3"
musica_de_fundo = pygame.mixer.music.load(localmusica)
pygame.mixer.music.play(-1) 


jogador1 = jogador( 0,0,(255,0,0),40,40)
frutinha = jogador(randint(5,10),randint(5,10),(0,0,255),40,40)
pontuacao = 0
clock = pygame.time.Clock()
velociade_de_andar = 15
fonte = pygame.font.SysFont('arial',40,True,True)


running = True
while running :
    clock.tick(60)
    tela.fill((0,0,0))
    mensagem = f"Pontos:{pontuacao}"
    textoformatado = fonte.render(mensagem,True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if pygame.key.get_pressed()[K_d] == True:
            jogador1.player_x+=velociade_de_andar
        if pygame.key.get_pressed()[K_a] == True:
            jogador1.player_x-=velociade_de_andar
        if pygame.key.get_pressed()[K_w] == True:
            jogador1.player_y-=velociade_de_andar
        if pygame.key.get_pressed()[K_s] == True:
            jogador1.player_y+=velociade_de_andar
    
    Jogado1 = pygame.draw.rect(tela,(255,0,0), (jogador1.player_x,jogador1.player_y,jogador1.player_largura,jogador1.player_largura))
    Frutinha = pygame.draw.rect(tela,(255,0,0), (frutinha.player_x,frutinha.player_y,frutinha.player_largura,frutinha.player_largura))
    
    def pega_aleatorio():
        valor_aleatorio1=randint(1,720)
        valor_aleatorio2=randint(1,480)
        return valor_aleatorio1 & valor_aleatorio2
    
    if Frutinha.colliderect(Jogado1):
        frutinha.player_x = pega_aleatorio()
        frutinha.player_y = pega_aleatorio()
        pontuacao += 1
       
        
    tela.blit(textoformatado,(50,40))
    pygame.display.update()