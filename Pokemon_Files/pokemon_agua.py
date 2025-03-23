# Importacao
from colorama import Fore
from random import randint

# Diretorio
from Pokemon_Files.pokemon import Pokemon

"""
# SUB CLASSE: POKEMON_AGUA
"""

class Pokemon_Agua(Pokemon):

    # Construtor que herda de Pokemon e define o tipo como "agua"
    def __init__(self, especie, nome=None, level=None):

        super().__init__(especie=especie, nome=nome, level=level)

        # Define o tipo do Pokémon como água
        self.tipo = "agua"


    # Metodo de ataque específico para Pokémon de tipo Água
    def atacar(self, pokemon_rival):

        # Escolhe um ataque aleatório
        rand = randint(1, 5)

        # Exibe a ação do ataque com base no número aleatório gerado
        if rand == 1:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou um {Fore.CYAN}"
                  f"Jato de Agua{Fore.RESET} em {pokemon_rival}")

        elif rand == 2:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou uma {Fore.CYAN}"
                  f"Bomba de Agua{Fore.RESET} em {pokemon_rival}")

        elif rand == 3:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou um {Fore.CYAN}"
                  f"Surf{Fore.RESET} em {pokemon_rival}")

        elif rand == 4:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou uma {Fore.CYAN}"
                  f"Hidro Bomba{Fore.RESET} em {pokemon_rival}")

        elif rand == 5:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou um {Fore.CYAN}"
                  f"Golpe de Agua{Fore.RESET} em {pokemon_rival}")

        # Chama o metodo de ataque da classe pai (Pokemon) para aplicar dano
        return super().atacar(pokemon_rival)