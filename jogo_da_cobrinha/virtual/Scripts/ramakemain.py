from PySide6.QtWidgets import QApplication, QPushButton
import pygame
from pygame.locals import *
from random import randint # Importa o randint para pegar numero aleatorio, para posição da frutinha


pygame.init()
pygame.mixer.init()

#Define os locais que estao os sons
local_musica = "Python projects//jogo_da_cobrinha/virtual//sons//doom.mp3"
local_son_pegou_frutinha = "Python projects//jogo_da_cobrinha/virtual//sons//pegou.mp3"
local_son_bateu_na_parede = "C:\\Users\\teste\\Documents\\Programação\\python-projets\\jogo_da_cobrinha\\virtual\\Scripts\\jogo_da_cobrinha\\sons\\bateu_na_parede.mp3"

musica_de_fundo = pygame.mixer.music.load(local_son_bateu_na_parede)
pygame.mixer.music.play(-1)

posicao_aleatorio_x = randint(0,480)
posicao_aleatorio_y = randint(0,720)

#Definir jogador e a frutinhe || Defini a cor
vermelho = (255,0,0)
verde = (0,255,0)
Jogador = objeto(0,0,vermelho,20,20)
Frutinha = objeto(posicao_aleatorio_x,posicao_aleatorio_y,verde,20,20)

#Cria a variavel pontuação 
pontuacao = 0



