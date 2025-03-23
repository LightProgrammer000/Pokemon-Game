# Importacao
from colorama import Fore
from random import randint

# Diretorio
from Pokemon_Files.pokemon import Pokemon

"""
# SUB CLASSE: POKEMON_FOGO
"""

class Pokemon_Fogo(Pokemon):

    # Construtor que herda de Pokemon e define o tipo como "fogo"
    def __init__(self, especie, nome=None, level=None):

        super().__init__(especie=especie, nome=nome, level=level)

        # Define o tipo do Pokémon como fogo
        self.tipo = "fogo"

    # Metodo de ataque específico para Pokémon de tipo Fogo
    def atacar(self, pokemon_rival):

        # Escolhe um ataque aleatório
        rand = randint(1, 5)

        # Exibe a ação do ataque com base no número aleatório gerado
        if rand == 1:
            print(f"{self} {Fore.LIGHTRED_EX}lancou uma {Fore.RED}Chama{Fore.RESET} em {pokemon_rival}")

        elif rand == 2:
            print(f"{self} {Fore.LIGHTRED_EX}lancou uma {Fore.RED}Lanca Chamas{Fore.RESET} em {pokemon_rival}")

        elif rand == 3:
            print(f"{self} {Fore.LIGHTRED_EX}lancou uma {Fore.RED}Explosao de Fogo{Fore.RESET} em {pokemon_rival}")

        elif rand == 4:
            print(f"{self} {Fore.LIGHTRED_EX}lancou uma {Fore.RED}Chama da Fenix{Fore.RESET} em {pokemon_rival}")

        elif rand == 5:
            print(f"{self} {Fore.LIGHTRED_EX}lancou um {Fore.RED}Giro Fogo{Fore.RESET} em {pokemon_rival}")

        # Chama o metodo de ataque da classe pai (Pokemon) para aplicar dano
        return super().atacar(pokemon_rival)
