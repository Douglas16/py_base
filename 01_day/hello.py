#!/usr/bin/env python3

'''

Filosofia da Linguagem ( Zen of Python ) PEP 20

Bonito é melhor que feio.
Explícito e melhor que implícito.
Simples e melhor que Complexo.
Complexo é melhor que Complicado.
Linear é melhor do que Aninhado.
Esparso é melhor que Denso.
Legibilidade Conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Anda que praticidade vença a pureza.
Erros nunca devem passar sileciosamente.
A menos que sejam explicitamente silencioados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deveria haver um - E prefrencialmente só um - Modo óbvio para fazer algo
Embora esse modo possa não ser óbvio a princípio, a menos que você seja holondês.
Agora é melhor que nunca, embora nunca frequenctemente seja melhor que imediatemente.
Se a implementação é dificil de explicar, é uma má ideia. se for fácil de explicar, pode ser uma boa ideia.


'''

# Hello World Multi Linguas.
# Usage: LANG env
# export LANH=pt_BR
#  

__version__ = "0.0.1"
__author__ = "Douglas Desiderio"
__license__ = "Unlicense"

import os 

# LANG=C.UTF-8
# snake Case
current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"


if current_language == "pt_BR":
    msg = "Ola Mundo!"

elif current_language =="it_IT":
    msg = "Ciao, Mondo!"
elif current_language =="es_SP":
    msg ="Hola, Mundo!"
elif current_language =="de_DE":
    msg = "Hallo Welt!"
elif current_language == "fr_FR":
    msg = "Bounjour Monde!"



# Ficando obsoleto
if __name__ == "__main__":
    print(msg)

# LANG=it_IT python3 hello.py









