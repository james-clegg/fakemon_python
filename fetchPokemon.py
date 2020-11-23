import requests
import asyncio
import json
import random

class FetchPokemon:
    def __init__(self):
        pass


    def startUpPrintStatements(self):
        print("Welcome to Pokemon - you will each choose 3 pokemon so please take turns.")


    def getAllKantoPokemon(self):
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
        responseJson = response.json()
        return responseJson['results']


    def getChosenPokemon(self, chosenPokemon, allpokemon):
        for pokemon in allpokemon:
            if pokemon['name'] == chosenPokemon['name']:
                response = requests.get(pokemon['url'])
                return self.__formatPokemon(response.json())


    def __formatPokemon(self, chosenPokemon):
        pokemonToReturn = {}
        pokemonType1 = chosenPokemon['types'][0]['type']['name']
        pokemonToReturn = {
            'name': chosenPokemon['name'],
            'types': [pokemonType1],
            'moves': self.__pickRandomMoveset(chosenPokemon)
        }
        if len(chosenPokemon['types']) > 1:
            pokemonType2 = chosenPokemon['types'][1]['type']['name']
            pokemonToReturn['types'].append(pokemonType2)
        return pokemonToReturn


    def __pickRandomMoveset(self, pokemon):
        pokemonPossibleMoveList = pokemon['moves']
        pokemonActualMoveDict = {}
        mv1 = self.__makeMoveRequest(pokemonPossibleMoveList)
        mv2 = self.__makeMoveRequest(pokemonPossibleMoveList)
        mv3 = self.__makeMoveRequest(pokemonPossibleMoveList)
        mv4 = self.__makeMoveRequest(pokemonPossibleMoveList)
        pokemonActualMoveDict = {
            'mv1': {
                'name': mv1['name'],
                'damage': mv1['power'],
                'type': mv1['type']['name']
            },
            'mv2': {
                'name': mv2['name'],
                'damage': mv2['power'],
                'type': mv2['type']['name']
            },
            'mv3': {
                'name': mv3['name'],
                'damage': mv3['power'],
                'type': mv3['type']['name']
            },
            'mv4': {
                'name': mv4['name'],
                'damage': mv4['power'],
                'type': mv4['type']['name']
            },
        }
        return pokemonActualMoveDict


    def __makeRandomNum(self, len):
        return random.randint(0, len)


    def __makeMoveRequest(self, possibleMvList):
        pokemonMove = requests.get(possibleMvList[self.__makeRandomNum(len(possibleMvList)-1)]['move']['url']).json()
        if type(pokemonMove['power']) != int:
            return self.__makeMoveRequest(possibleMvList)
        pokemonMoveToReturn = {
            'name' : pokemonMove['name'],
            'power' : pokemonMove['power'],
            'type' : pokemonMove['type']
        }
        return pokemonMoveToReturn
