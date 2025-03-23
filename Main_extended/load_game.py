"""
# Carregar Jogo
"""

# Importações necessárias
from pickle import load
from colorama import Fore

def loading():

    # Caminho do arquivo de dados do jogo
    memory_card = "Main_extended/memory_card.csv"

    try:

        # Tenta abrir o arquivo para leitura binária
        with open(memory_card, "rb") as file:
            print(f"{Fore.LIGHTBLUE_EX}Loading...{Fore.RESET}")

            # Carrega o conteúdo do arquivo usando pickle
            return load(file)

    except FileNotFoundError:

        # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
        print(f"{Fore.LIGHTWHITE_EX}Loading... Failed !!!{Fore.RESET}")

        # Retorna None caso não seja possível carregar o jogo
        return None