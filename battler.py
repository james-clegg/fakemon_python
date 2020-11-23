from pokemonCreator import Pokemon
from battleCreator import BattleCreator
from pokemonChooser import PokemonChooser
from printPokemonArt import PrintPokemonArt
from partyCreator import PartyCreator
from fetchPokemon import FetchPokemon


printArtobj = PrintPokemonArt()
party1 = PartyCreator()
party2 = PartyCreator()
newFetch = FetchPokemon()
allPokemon = newFetch.getAllKantoPokemon()
newChooser = PokemonChooser(allPokemon)
printArtobj.printAsciiArt()
newFetch.startUpPrintStatements()


for _x in range(0, 3):
    party1.addPokemonToParty(Pokemon(newChooser.choosePokemon(allPokemon)))
    party2.addPokemonToParty(Pokemon(newChooser.choosePokemon(allPokemon)))
newBattle = BattleCreator(party1, party2)


while(True):
    newBattle.turnPlayerMove()
