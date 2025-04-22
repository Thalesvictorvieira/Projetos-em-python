import random
import string


a = list(string.ascii_lowercase)

key_word = "TESTE"
key_word.lower()
tamanho = len(key_word)
letras_possiveis = a

palavra_gerada = ['_' for _ in range(tamanho)]
letras_testadas_por_posicao = [set() for _ in range(tamanho)]

tentativas = 0
pos = 0

while ''.join(palavra_gerada) != key_word:
    opcoes_validas = [l for l in letras_possiveis if l not in letras_testadas_por_posicao[pos]]
    if not opcoes_validas:
        break

    letra = random.choice(opcoes_validas)
    tentativas += 1
    letras_testadas_por_posicao[pos].add(letra)

    print(f"Tentativa {tentativas}: letra '{letra}'")

    if letra == key_word[pos]:
        palavra_gerada[pos] = letra
        pos += 1

print(f"\nPalavra final encontrada: {''.join(palavra_gerada)} em {tentativas} tentativas.")
