"""
# Deletar Arquivo - Reiniciar Jogo
"""

# Importações necessárias
from os import remove
from os.path import exists
from colorama import Fore

def reiniciar_jogo():

    try:
        # Caminho do arquivo de dados do jogo
        memory_card = "Main_extended/memory_card.csv"

        # Verifica se o arquivo existe
        if exists(memory_card):

            # Solicita confirmação para apagar os dados
            esc = input(f"{Fore.LIGHTRED_EX}Dados serão apagados permanentemente [s] [n]: {Fore.RESET}").lower()

            # Caso o usuário confirme a exclusão
            if esc == "s":
                remove(memory_card)
                print(f"{Fore.LIGHTMAGENTA_EX}Jogo foi reiniciado com sucesso, favor executar novamente!{Fore.RESET}")

            elif esc == "n":
                print(f"{Fore.LIGHTBLUE_EX}Jogo não reiniciado!{Fore.RESET}")

        else:
            # Se o arquivo não existir
            print(f"{Fore.LIGHTYELLOW_EX}Arquivo de dados não encontrado. Jogo não reiniciado!{Fore.RESET}")

    # Captura de exceções genéricas para evitar falhas
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Ocorreu um erro ao tentar reiniciar o jogo: {e}{Fore.RESET}")
