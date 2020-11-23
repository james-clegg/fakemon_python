
class PartyCreator:
    def __init__(self):
        self.currentParty = []


    def addPokemonToParty(self, pokemon):
        self.currentParty.append(pokemon)


    def removePokemonFromParty(self, pokemon):
        self.currentParty.remove(pokemon)


    def printCurrentParty(self, currentPokemon):
        print("Here are your available pokemon: ")
        for pokemon in self.currentParty:
            if pokemon != currentPokemon:
                print(pokemon.name.capitalize())


    def switchActivePokemon(self, pokemon):
        self.currentParty.insert(0, self.currentParty.pop(self.currentParty.index(pokemon)))
