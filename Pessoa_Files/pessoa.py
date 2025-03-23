# Biblioteca
from time import sleep
from colorama import Fore
from random import choice, sample, randint

# Diretorio
from Pokemon_Files.pokemon_agua import Pokemon_Agua
from Pokemon_Files.pokemon_fogo import Pokemon_Fogo
from Pokemon_Files.pokemon_eletrico import Pokemon_Eletrico

"""
# CLASSE: PESSOA
"""

class Pessoa:

    def __init__(self, nome=None, pokemons=None, dinheiro=100):

        self.nome = nome_aleatorios() if nome is None else nome
        self.pokemons = pokemons if pokemons is not None else []
        self.dinheiro = dinheiro


    def __str__(self):
        return f"{Fore.LIGHTGREEN_EX}{self.nome}{Fore.RESET}"


    """ Metodos Principais """
    def mostrar_pokemon(self):

        if len(self.pokemons) > 0:
            print(f"| Pokemon(s) de {self} |")

            # Enumerando pokemons
            for i, j in enumerate(self.pokemons):
                print(f"{i}: {j}")

        else:
            print(f"{self} {Fore.RED}nao possui pokemons{Fore.RESET}")


    # Metodo: Escolha de pokemons de maneira automatica
    def escolher_pokemon(self):

        if len(self.pokemons) > 0:
            pokemon_rival_escolhido = choice(self.pokemons)

            print(f"{self} escolheu {pokemon_rival_escolhido}")
            return pokemon_rival_escolhido

        else:
            print(f"{self} esta sem pokemons para a batalha !")
            return None


    def batalhar(self, rival):

        print(f"{self} iniciou uma batalha com {rival}")

        # Mostrar Pokemons do adversario + escolha automatica
        rival.mostrar_pokemon()
        pokemon_rival = rival.escolher_pokemon()

        # Escolha do Player
        self.mostrar_pokemon()
        pokemon = self.escolher_pokemon()

        # Verificacao do resultado da batalha
        if pokemon and pokemon_rival:

            while True:
                sleep(1)

                if pokemon.atacar(pokemon_rival):

                    print(f"{self} ganhou a batalha")
                    self.ganhar_dinheiro(pokemon_rival.level * 10)
                    break

                if pokemon_rival.atacar(pokemon):

                    print(f"{self} perdeu a batalha")
                    self.perder_dinheiro(pokemon.level * 10)
                    break

        else:
            print("Batalha Cancelada !")


    def explorar(self):

        # Chance de encontrar Pokemons selvagens
        if randint(1, 10) <= 3:

            pokemon = choice(lista_pokemons_aleatorios())
            print(f"Um Pokemon {pokemon} selvagem apareceu!")

            resp = input("Deseja capturá-lo? [s] / [n]: ").lower()

            if resp == "s":

                # Chance de captura baseada no nível do Pokémon
                chance_captura = max(30, 100 - (pokemon.level * 10) + self.calcular_bonus_de_captura() * 5)

                if randint(1, 100) <= chance_captura:

                    print(f"{self} capturou {pokemon}!")
                    self.pokemons.append(pokemon)
                    self.mostrar_pokemon()

                else:
                    print(f"{Fore.GREEN}Pokemon escapou!{Fore.RESET}")

            else:
                print("Voce decidiu nao capturar o Pokemon.")

        else:
            print(f"{Fore.RED}Exploracao sem sucesso!{Fore.RESET}")


    """"""""""""""""""""""""""""""""""""
    """ Metodos de suporte a Classe """
    """"""""""""""""""""""""""""""""""""

    def mostrar_dinheiro(self):
        print(f"{self} possui R$ {self.dinheiro}")


    def ganhar_dinheiro(self, montante):

        self.dinheiro += montante
        print(f"{self} ganhou R$ {montante}")
        self.mostrar_dinheiro()


    def perder_dinheiro(self, montante):

        self.dinheiro -= montante
        print(f"{self} perdeu R$ {montante}")

        if self.dinheiro < 0:
            self.dinheiro = 0
            self.mostrar_dinheiro()


    def calcular_bonus_de_captura(self):

        if self.pokemons:

            # Retorna o maior nivel diretamente
            return max(i.level for i in self.pokemons)

        else:
            return 0


""""""""""""""""""""""""""
""" Metodos de suporte """
""""""""""""""""""""""""""

def nome_aleatorios():

    nomes = [
        "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas",
        "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua",
        "Kenneth", "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward", "Jason", "Jeffrey", "Ryan",
        "Gary", "Nicholas", "Eric", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel",
        "Frank", "Gregory", "Alexander", "Raymond", "Patrick", "Jack", "Dennis", "Jerry", "Tyler", "Aaron",
        "Jose", "Adam", "Zachary", "Nathan", "Peter", "Harold", "Douglas", "Kyle", "Walter", "Ethan",
        "Carl", "Arthur", "Gerald", "Roger", "Joe", "Juan", "Jackie", "Christian", "Roy", "Bobby", "Albert",
        "Russell", "Mason", "Dylan", "Lucas", "Henry", "Wayne", "Eugene", "Ralph", "Juan", "Billy", "Bruce",
        "Willie", "Jordan", "Carl", "Dean", "Alan", "Randy", "Craig", "Danny", "Victor", "Lee", "Melvin",
        "Leonard", "Curtis", "Ernest", "Chad", "Francis", "Herman", "Claude", "Edwin", "Charlie", "Brett",
        "Bill", "Leroy", "Todd", "Danny", "Arthur", "Dennis", "Marvin", "Alfred", "Wesley", "Clifford",
        "Calvin", "Martin", "Ruben", "Tony", "Harry", "Glen", "Howard", "Manuel", "Theodore", "Norman"
    ]

    return choice(nomes)


def lista_pokemons_aleatorios():

    pokemons_fogo = [
        "Charizard", "Blaziken", "Infernape", "Emboar", "Volcarona", "Arcanine", "Houndoom", "Darmanitan", "Camerupt",
        "Flareon", "Magmortar", "Chandelure", "Talonflame", "Centiskorch", "Reshiram", "Ho-Oh", "Moltres", "Heatran",
        "Blacephalon", "Entei", "Cinderace", "Delphox", "Torkoal", "Simisear", "Pyroar", "Magmar", "Ninetales-Alola",
        "Zoroark", "Darumaka", "Zorua", "Zekrom", "Moltres-Galar", "Chandelure", "Centiskorch", "Litten", "Volcarona",
        "Torkoal", "Blaziken", "Camerupt", "Flareon", "Cinderace", "Infernape", "Simisear", "Salamence", "Magmortar",
        "Reshiram", "Moltres-Galar", "Pyroar", "Emboar", "Darmanitan", "Talonflame", "Centiskorch", "Camerupt",
        "Volcarona", "Arcanine", "Ho-Oh", "Magmar", "Ninetales-Alola", "Delphox", "Magmortar", "Houndoom", "Zoroark",
        "Zekrom", "Entei", "Blacephalon", "Tepig", "Flareon", "Darumaka", "Talonflame", "Houndoom", "Simisear",
        "Centiskorch", "Zekrom", "Salamence", "Cinderace", "Tepig", "Blaziken", "Darmanitan", "Emboar", "Ho-Oh",
        "Reshiram", "Magmortar", "Flareon", "Magmar", "Torkoal", "Volcarona", "Pyroar", "Simisear", "Infernape",
        "Torkoal"
    ]

    pokemons_agua = [
        "Swampert", "Empoleon", "Incineroar", "Gyarados", "Vaporeon", "Ludicolo", "Kingdra", "Milotic", "Gastrodon",
        "Feraligatr", "Greninja", "Barbaracle", "Blastoise", "Samurott", "Toxapex", "Crawdaunt", "Seaking", "Quagsire",
        "Sharpedo", "Starmie", "Kingler", "Corsola", "Carvanha", "Marill", "Azumarill", "Basculin", "Corphish",
        "Remoraid", "Octillery", "Wailord", "Swampert", "Politoed", "Lapras", "Kabutops", "Lanturn", "Clawitzer",
        "Lileep", "Seviper", "Finneon", "Lumineon", "Dewgong", "Shellder", "Horsea", "Magikarp", "Totodile",
        "Chinchou", "Barboach", "Squirtle", "Piplup", "Totodile", "Kip", "Lugia", "Pelipper", "Tentacool",
        "Tentacruel", "Sharpedo", "Vaporeon", "Dratini", "Dragapult", "Basculin", "Marill", "Gyarados", "Blastoise",
        "Greninja", "Lanturn", "Politoed", "Sharpedo", "Corsola", "Clawitzer", "Dewgong", "Wailord", "Quagsire",
        "Carvanha", "Swampert", "Surskit", "Barboach", "Starmie", "Remoraid", "Seaking", "Magikarp", "Barbaracle",
        "Feraligatr", "Kingdra", "Milotic", "Seviper"
    ]

    pokemons_eletrico = [
        "Raikou", "Electivire", "Zekrom", "Thundurus", "Luxray", "Jolteon", "Ampharos", "Magnezone", "Eelektross",
        "Zeraora", "Rotom", "Shinx", "Chinchou", "Pachirisu", "Raichu", "Elekid", "Magnemite", "Emolga", "Minun",
        "Plusle", "Electrike", "Galvantula", "Helioptile", "Heliolisk", "Mareep","Zapdos", "Pikachu", "Voltorb",
        "Electrode", "Tynamo", "Pichu", "Rotom-Wash", "Magneton", "Heliolisk", "Zeraora", "Luxray", "Electivire",
        "Galvantula", "Raikou", "Thundurus", "Eelektross", "Zapdos", "Raichu", "Electrike", "Jolteon", "Luxray",
        "Rotom", "Zekrom", "Shinx", "Elekid", "Pikachu", "Zeraora", "Electivire", "Magnezone", "Voltorb", "Electrode",
        "Raikou", "Zapdos", "Thundurus", "Rotom", "Jolteon", "Luxray", "Eelektross", "Magnezone", "Tynamo",
        "Electrike", "Raichu", "Galvantula", "Heliolisk", "Mareep", "Zeraora", "Zekrom", "Electivire", "Pichu",
        "Elekid"
    ]

    fogo_ale =     sample(pokemons_fogo, 2)
    agua_ale =     sample(pokemons_agua, 2)
    eletrico_ale = sample(pokemons_eletrico, 2)

    # Listagem com os pokemons escolhidos
    lista_pokemons = [
        Pokemon_Fogo(fogo_ale[0]), Pokemon_Fogo(fogo_ale[1]),
        Pokemon_Agua(agua_ale[0]), Pokemon_Agua(agua_ale[1]),
        Pokemon_Eletrico(eletrico_ale[0]), Pokemon_Eletrico(eletrico_ale[1])
    ]

    return lista_pokemons
