# Bibliotecas
from random import randint, choice

# Diretorio
from Pessoa_Files.pessoa import Pessoa, lista_pokemons_aleatorios

"""
# SUBCLASSE: INIMIGO
"""
class Inimigo(Pessoa):

    # Construtor da classe Inimigo
    def __init__(self, nome=None, pokemons=None, dinheiro=100):

        # Chama o construtor da classe pai (Pessoa)
        super().__init__(nome=nome, pokemons=pokemons, dinheiro=dinheiro)

        # Define o tipo como "inimigo"
        self.tipo = "inimigo"

        # Se não for passado uma lista de pokemons, gera automaticamente
        if pokemons is None:

            # Determina quantos pokemons o inimigo terá (1 a 6)
            numero_pokemons = randint(1, 6)

            # Obtém uma lista de pokemons aleatórios
            pokemons_disponiveis = lista_pokemons_aleatorios()

            # Adiciona pokemons à lista do inimigo
            for i in range(numero_pokemons):

                # Escolhe um pokemon aleatório
                escolha_pokemon_random = choice(pokemons_disponiveis)

                # Adiciona o pokemon à lista do inimigo
                self.pokemons.append(escolha_pokemon_random)

                # Remove o pokemon da lista para evitar repetição
                pokemons_disponiveis.remove(escolha_pokemon_random)

        else:

            # Se os pokemons foram passados, usa-os diretamente
            self.pokemons = pokemons
