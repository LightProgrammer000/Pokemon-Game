"""
# Salvar Jogo
"""

# Importações necessárias
from pickle import dump
from colorama import Fore

def saving(player):

    # Caminho do arquivo onde os dados do jogo serão salvos
    memory_card = "Main_extended/memory_card.csv"

    try:
        # Tenta abrir o arquivo para escrita binária
        with open(memory_card, "wb") as file:

            # Serializa e salva o objeto 'player' no arquivo
            dump(player, file)
            print(f"{Fore.LIGHTGREEN_EX}Jogo salvo com sucesso!{Fore.RESET}")

    except FileNotFoundError:

        # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
        print(f"{Fore.LIGHTRED_EX}Falha ao salvar o jogo! Arquivo não encontrado.{Fore.RESET}")
