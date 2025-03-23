# Importações
from Support.importacoes import  *

def main():

    try:
        # Mensagem de boas-vindas
        print("-----------------------------------------")
        print(f"{Fore.LIGHTGREEN_EX}Bem-Vindo ao Game Pokemon RPG de Terminal{Fore.RESET}")
        print("-----------------------------------------")

        # Tentativa de carregar o jogador salvo
        player = loading()

        # Caso não tenha um jogador salvo, cria um novo
        if player is None:
            nome = input("\nOla, qual seu nome: ")
            player = Player(nome=nome)

            print(f"Ola {player}, esse e um mundo habitado por pokemons, a partir de agora sua missao "
                  f"e se tornar um mestre dos pokemons")
            print("Capture o maximo de pokemons que conseguir e lute contra seus inimigos")

            player.mostrar_dinheiro()
            print("")

        # Mostra os pokemons que o jogador já possui
        if len(player.pokemons) > 0:

            print("Notei que voce tem alguns pokemons")
            player.mostrar_pokemon()

        else:
            print(f"Notei que voce {player}, nao tem nenhum pokemon, portanto precisa escolher um")
            escolher_pokemon_inicial(player=player)

            print("Muito bem! Agora que ja voce possui um pokemon, "
                  "enfrente seu arqui-rival Gary desde o jardim da infancia")

            # Criando e batalhando com o inimigo Gary
            gary = Inimigo(nome="Gary", pokemons=[Pokemon_Agua("Squirtle", level=1)])
            player.batalhar(gary)

            # Salvando o jogo após a batalha
            saving(player=player)

        # Menu principal enquanto o jogador estiver no jogo
        while True:

            try:
                print("\nO que deseja fazer ?")
                print(f"{Fore.LIGHTGREEN_EX}[1] Explorar pelo mundo a fora{Fore.RESET}")
                print(f"{Fore.LIGHTRED_EX}[2] Lutar com um inimigo{Fore.RESET}")
                print(f"{Fore.LIGHTBLUE_EX}[3] PokeAgenda{Fore.RESET}")
                print(f"{Fore.LIGHTYELLOW_EX}[4] Novo jogo{Fore.RESET}")
                print(f"{Fore.LIGHTMAGENTA_EX}[0] Sair / Salvar Jogo{Fore.RESET}")
                opc = int(input("Opc.: "))

                # Opções de ações do jogador
                if opc == 1:
                    player.explorar()

                elif opc == 2:
                    player.batalhar(Inimigo())

                elif opc == 3:
                    player.mostrar_pokemon()

                elif opc == 4:
                    reiniciar_jogo()
                    break

                elif opc == 0:
                    print(f"{Fore.LIGHTGREEN_EX}Saving...{Fore.RESET}")
                    break

                elif opc == 100:
                    print(f"{Fore.BLACK}Hack Ativado ...{Fore.RESET}")
                    player.hack()

                else:
                    # Caso a opção seja inválida
                    print("Opcao inexistente!")

                # Salvando o progresso após qualquer ação
                saving(player=player)

            except ValueError:
                print("Opcao Invalida !")

    except KeyboardInterrupt:
        print(f"{Fore.LIGHTRED_EX}\nJogo finalizado !{Fore.RESET}")

if __name__ == '__main__':
    main()
