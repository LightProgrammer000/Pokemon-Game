# Importação
from colorama import Fore
from random import randint, random

"""
# CLASSE PAI: POKEMON
"""

class Pokemon:

    # Construtor inicializa os atributos do Pokémon
    def __init__(self, especie, nome=None, level=None):

        self.especie = especie
        self.nome = especie if nome is None else nome
        self.level = randint(1, 100) if level is None else level
        self.ataque = self.level * 5
        self.vida = self.level * 10


    # Metodo que retorna a string de apresentação do Pokémon
    def __str__(self):
        return f"{Fore.LIGHTCYAN_EX}{self.especie}{Fore.RESET} {Fore.LIGHTYELLOW_EX}({self.level}){Fore.RESET}"


    # Metodo de ataque contra outro Pokémon
    def atacar(self, pokemon_rival):

        # # Cálculo do dano com aleatoriedade
        ataque_efetivo = int(self.ataque * random() * 1.3)

        # Tipos de ataques (Água vs Fogo, Elétrico vs Água, etc)
        if self.tipo == "agua" and pokemon_rival.tipo == "fogo":

            # Aumento de dano (Água vs Fogo)
            ataque_efetivo = int(ataque_efetivo * 1.2)

        elif self.tipo == "fogo" and pokemon_rival.tipo == "agua":

            # Redução de dano (Fogo vs Água)
            ataque_efetivo = int(ataque_efetivo * 0.5)

        elif self.tipo == "eletrico" and pokemon_rival.tipo == "agua":

            # Aumento de dano (Elétrico vs Água)
            ataque_efetivo = int(ataque_efetivo * 1.2)

        elif self.tipo == "agua" and pokemon_rival.tipo == "eletrico":

            # Redução de dano (Água vs Elétrico)
            ataque_efetivo = int(ataque_efetivo * 0.5)

        # Aplica o dano no Pokémon rival
        pokemon_rival.vida -= ataque_efetivo
        print(f"{pokemon_rival} perdeu {ataque_efetivo} pontos de vida")

        # Verifica se o Pokémon rival foi derrotado
        if pokemon_rival.vida <= 0:

            print(f"{pokemon_rival} foi {Fore.LIGHTRED_EX}derrotado !{Fore.RESET}")

            # Retorna True se o Pokémon rival foi derrotado
            return True

        else:

            # Retorna False se o Pokémon rival ainda estiver vivo
            return False