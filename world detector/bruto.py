import string
import random

Key_world = "feijao"
a = list(string.ascii_lowercase)
tentativa = ''
tentativas = 0

while tentativa != Key_world:
    tentativa = ''.join(random.choice(a) for _ in range(len(Key_world)))
    tentativas += 1
    print(f"Tentativa {tentativas}: {tentativa}")

print(f"Palavra encontrada após {tentativas} tentativas: {tentativa}")
