# Importacao
from colorama import Fore
from random import randint

# Diretorio
from Pokemon_Files.pokemon import Pokemon

"""
# SUB CLASSE: POKEMON_ELETRICO
"""

class Pokemon_Eletrico(Pokemon):

    # Construtor que herda de Pokemon e define o tipo como "eletrico"
    def __init__(self, especie, nome=None, level=None):

        super().__init__(especie=especie, nome=nome, level=level)

        # Define o tipo do Pokémon como eletrico
        self.tipo = "eletrico"


    def atacar(self, pokemon_rival):

        # Escolhe um ataque aleatório
        rand = randint(1, 5)

        # Exibe a ação do ataque com base no número aleatório gerado
        if rand == 1:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou um {Fore.LIGHTCYAN_EX}"
                  f"Choque do Trovao{Fore.RESET} em {pokemon_rival}")

        elif rand == 2:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou um {Fore.LIGHTBLUE_EX}"
                  f"Raio{Fore.RESET} em {pokemon_rival}")

        elif rand == 3:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou um {Fore.LIGHTMAGENTA_EX}"
                  f"Relampago{Fore.RESET} em {pokemon_rival}")

        elif rand == 4:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou uma {Fore.LIGHTGREEN_EX}"
                  f"Corte Eletrico{Fore.RESET} em {pokemon_rival}")

        elif rand == 5:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou um {Fore.LIGHTRED_EX}"
                  f"Pulso Eletrico{Fore.RESET} em {pokemon_rival}")

       # Chama o metodo de ataque da classe pai (Pokemon) para aplicar dano
        return super().atacar(pokemon_rival)