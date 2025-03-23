# Bibliotecas
from colorama import Fore

# Diretório
from Pessoa_Files.pessoa import Pessoa
from Pokemon_Files.pokemon_eletrico import Pokemon_Eletrico
from sympy.codegen.ast import continue_

"""
# SUBCLASSE: PLAYER
"""

class Player(Pessoa):

    # Construtor da classe Player
    def __init__(self, nome=None, pokemons=None, dinheiro=100):

        # Chama o construtor da classe pai (Pessoa)
        super().__init__(nome=nome, pokemons=pokemons, dinheiro=dinheiro)

        self.tipo = "player"


    # Metodo para o jogador escolher um Pokémon
    def escolher_pokemon(self):

        global pokemon_escolhido

        while True:

            try:
                # Verifica se o jogador tem pokemons
                if len(self.pokemons) > 0:

                        # Solicita ao jogador que escolha o indice do seu Pokemon
                        escolha_indice_pokemon = int(input("Escolha o indice referente ao seu Pokemon: "))

                        # Acessa o Pokemon escolhido através do índice
                        pokemon_escolhido = self.pokemons[escolha_indice_pokemon]

                        # Exibe a escolha do Pokémon
                        print(f"{pokemon_escolhido} eu escolho você!!!")

                else:
                    print(f"{self} sem pokemon para a batalha!")
                    return None

            # Trata exceções de índice inválido ou valor inválido
            except (IndexError, ValueError):
                print(f"{Fore.LIGHTRED_EX}Selecao invalida! Tente novamente.{Fore.RESET}")
                continue

            return pokemon_escolhido


    # Metodo para o jogador capturar um Pokémon
    def capturar_pokemon(self, pokemon):

        print(f"{Fore.LIGHTBLUE_EX}{self} capturou {pokemon}{Fore.RESET}")

        # Adiciona o Pokémon à lista do jogador
        self.pokemons.append(pokemon)


    # Metodo para o jogador "hackear" um Pokémon
    def hack(self):

        # Cria o Pokémon Zapdos com nível 100
        zapdos = Pokemon_Eletrico(especie="Zapdos", level=1000)

        # Adiciona o Zapdos à lista de pokémons do jogador
        self.pokemons.append(zapdos)
