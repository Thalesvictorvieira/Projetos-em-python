import pygame
from pygame.locals import *
from random import randint
from classes import objeto

# Inicializa o pygame
pygame.init()
pygame.mixer.init()

# Define os locais dos sons
local_musica = "C:\\Users\\teste\\Documents\\Desinvilvimento\\Projetos-em-python\\jogo_da_cobrinha\\virtual\\Scripts\\sons\\doom.mp3"
local_son_pegou_frutinha = "C:\\Users\\teste\\Documents\\Desinvilvimento\\Projetos-em-python\\jogo_da_cobrinha\\virtual\\Scripts\\sons\\pegou.wav"
local_son_bateu_na_parede = "C:\\Users\\teste\\Documents\\Desinvilvimento\\Projetos-em-python\\jogo_da_cobrinha\\virtual\\Scripts\\sons\\bateu_na_parede.mp3"

pygame.mixer.music.load(local_musica)
pygame.mixer.music.play(-1)  # Música de fundo

# Define as dimensões da janela
altura_janela = 720
largura_janela = 480
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Jogo da cobrinha')

# Define as cores
vermelho = (255, 0, 0)
verde = (0, 255, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

# Cria o jogador e a frutinha utilizando a classe objeto
jogador = objeto(0, 0, vermelho, 20, 20)
frutinha = objeto(randint(0, largura_janela - 20), randint(0, altura_janela - 20), verde, 20, 20)

# Define a fonte para a pontuação
fonte = pygame.font.SysFont('arial', 40, True, True)
velocidade = 15
relogio = pygame.time.Clock()

pontuacao = 0
rodando = True
corpo_jogador = []

# Função para crescer o jogador
def crescer_jogador(corpo_jogador):
    for x_y in corpo_jogador:
        pygame.draw.rect(tela, verde, (x_y[0], x_y[1], 20, 20))

# Função para gerar posições aleatórias dentro dos limites da janela
def posicao_aleatoria():
    x = randint(0, largura_janela - 20)
    y = randint(0, altura_janela - 20)
    return x, y

tamanho_jogador = 5
controle_x = 20
controle_y = 0

# Loop principal do jogo
while rodando:
    relogio.tick(9)
    tela.fill(preto)

    mensagem = f"Pontos: {pontuacao}"
    texto_formatado = fonte.render(mensagem, True, branco)

    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False

        # Movimento do jogador
        if event.type == KEYDOWN:
            if event.key == K_d and controle_x == 0:
                controle_x = 20
                controle_y = 0
            if event.key == K_a and controle_x == 0:
                controle_x = -20
                controle_y = 0
            if event.key == K_w and controle_y == 0:
                controle_y = -20
                controle_x = 0
            if event.key == K_s and controle_y == 0:
                controle_y = 20
                controle_x = 0

    # Atualiza a posição do jogador
    jogador.posicao_x += controle_x
    jogador.posicao_y += controle_y

    # Verifica se saiu dos limites da tela e reposiciona no lado oposto
    if jogador.posicao_x < 0:
        jogador.posicao_x = largura_janela - jogador.largura_obj
    elif jogador.posicao_x >= largura_janela:
        jogador.posicao_x = 0

    if jogador.posicao_y < 0:
        jogador.posicao_y = altura_janela - jogador.altura_obj
    elif jogador.posicao_y >= altura_janela:
        jogador.posicao_y = 0

    # Cria o jogador e a frutinha na tela
    jogado = pygame.draw.rect(tela, vermelho, (jogador.posicao_x, jogador.posicao_y, jogador.altura_obj, jogador.largura_obj))
    frutinha_rect = pygame.draw.rect(tela, verde, (frutinha.posicao_x, frutinha.posicao_y, frutinha.altura_obj, frutinha.largura_obj))

    # Verifica colisão com a frutinha
    if jogado.colliderect(frutinha_rect):
        frutinha.posicao_x, frutinha.posicao_y = posicao_aleatoria()
        pygame.mixer.Sound(local_son_pegou_frutinha).play()
        pontuacao += 1
        tamanho_jogador += 1

    # Atualiza o corpo do jogador
    cabeca_jogador = [jogador.posicao_x, jogador.posicao_y]
    corpo_jogador.append(cabeca_jogador)

    if len(corpo_jogador) > tamanho_jogador:
        del corpo_jogador[0]

    # Verifica colisão com o próprio corpo
    if cabeca_jogador in corpo_jogador[:-1]:
        pygame.mixer.Sound(local_son_bateu_na_parede).play()
        print("Game Over! Pontuação final:", pontuacao)
        rodando = False

    # Cresce o jogador
    crescer_jogador(corpo_jogador)

    # Renderiza a pontuação
    tela.blit(texto_formatado, (50, 40))
    pygame.display.update()

pygame.quit()
