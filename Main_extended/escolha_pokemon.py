"""
# Escolhendo Pokémon Inicial
"""

# Importações necessárias
from colorama import Fore
from Support.importacoes import *

def escolher_pokemon_inicial(player):

    # Criação dos Pokémon iniciais com nível 1
    pikachu = Pokemon_Eletrico(especie="Pikachu", level=1)
    charmander = Pokemon_Fogo(especie="Charmander", level=1)
    squirtle = Pokemon_Agua(especie="Squirtle", level=1)

    # Exibe as opções para o jogador
    print(f"# {player} escolha dentre 3 pokémons o seu pokémon inicial: ")
    print(f"[1] - {pikachu}")
    print(f"[2] - {charmander}")
    print(f"[3] - {squirtle}")
    print(f"[0] - Nenhum!")

    while True:

        try:
            # Solicita ao jogador que escolha uma opção
            opc = int(input("Escolha o seu Pokémon: "))
            print("")

            # Se o jogador escolher "Nenhum", o jogo será encerrado
            if opc == 0:
                print(f"{Fore.RED}NUNCA SERÁ UM MESTRE POKÉMON!!!{Fore.RESET}")
                exit(0)

            # Captura o Pokémon escolhido pelo jogador
            elif opc == 1:
                player.capturar_pokemon(pokemon=pikachu)

            elif opc == 2:
                player.capturar_pokemon(pokemon=charmander)

            elif opc == 3:
                player.capturar_pokemon(pokemon=squirtle)

            else:
                # Caso o jogador escolha uma opção inválida
                print(f"{Fore.YELLOW}# Vamos, capture seu Pokémon!!!{Fore.RESET}")
                continue

        except ValueError:
            # Captura caso o jogador insira algo que não seja um número
            print(f"{Fore.RED}Opção inválida! Tente novamente.{Fore.RESET}")
            continue

        # Encerra o loop após uma escolha válida
        break
