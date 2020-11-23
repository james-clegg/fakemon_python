import random
from fetchPokemon import FetchPokemon

class PokemonChooser:
    def __init__(self, pokemonSet):
        self.pokemonSet = pokemonSet


    def choosePokemon(self, allPokemon):
        response = input("Type the name of the pokemon you want to use, any of the original 151!\n")
        fetchObj = FetchPokemon()
        for pokemon in allPokemon:
            if response.lower() == pokemon['name']:
                print("---------------------------------------------------------------")
                return fetchObj.getChosenPokemon(pokemon, allPokemon)
        else:
            print("Sorry, you may have misspelt something. Here's a list of all 151 pokemon, please try again")
            for pokemon in allPokemon:
                print(pokemon['name'].capitalize())
            return self.choosePokemon(allPokemon)
