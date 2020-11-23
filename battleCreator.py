import sys

class BattleCreator:

    def __init__(self, pokemonList1, pokemonList2):
        self.pokemonList1 = pokemonList1
        self.pokemonList2 = pokemonList2
        self.turnPlayer = pokemonList1.currentParty[0]
        self.notTurnPlayer = pokemonList2.currentParty[0]
        self.turnCount = 1


    def __incrementTurnCount(self):
        self.turnCount += 1


    def __faintPokemon(self):
        print(self.notTurnPlayer.name + " fainted!")
        if self.notTurnPlayer in self.pokemonList1.currentParty:
            self.pokemonList1.removePokemonFromParty(self.notTurnPlayer)
            if len(self.pokemonList1.currentParty) == 0:
                self.__handleVictory(2)
            print(self.pokemonList1.currentParty[0].name + " entered the battle!")
        elif self.notTurnPlayer in self.pokemonList2.currentParty:
            self.pokemonList2.removePokemonFromParty(self.notTurnPlayer)
            if len(self.pokemonList2.currentParty) == 0:
                self.__handleVictory(1)
            print(self.pokemonList2.currentParty[0].name + " entered the battle!")


    def __changeTurnPlayer(self):
        if self.turnPlayer == self.pokemonList1.currentParty[0]:
            self.turnPlayer = self.pokemonList2.currentParty[0]
            self.notTurnPlayer = self.pokemonList1.currentParty[0]
        else:
            self.turnPlayer = self.pokemonList1.currentParty[0]
            self.notTurnPlayer = self.pokemonList2.currentParty[0]


    def __checkHP(self):
        if self.notTurnPlayer.hp <= 0:
            self.__faintPokemon()


    def __printListOfMoves(self):
        print("You can now choose a move to use from this list:")
        print(self.turnPlayer.mv1['name'].capitalize(), "| Type: " + self.turnPlayer.mv1['type'].capitalize(), "| Damage: " + str(self.turnPlayer.mv1['damage']))
        print(self.turnPlayer.mv2['name'].capitalize(), "| Type: " + self.turnPlayer.mv2['type'].capitalize(), "| Damage: " + str(self.turnPlayer.mv2['damage']))
        print(self.turnPlayer.mv3['name'].capitalize(), "| Type: " + self.turnPlayer.mv3['type'].capitalize(), "| Damage: " + str(self.turnPlayer.mv3['damage']))
        print(self.turnPlayer.mv4['name'].capitalize(), "| Type: " + self.turnPlayer.mv4['type'].capitalize(), "| Damage: " + str(self.turnPlayer.mv4['damage']))


    def __chooseMove(self):
        self.__printListOfMoves()
        response = input("Type the name of the move you want to use, or type 'switch' to switch your active pokemon:")
        if response.lower() == self.turnPlayer.mv1['name']:
            self.turnPlayer.useMv(self.notTurnPlayer, self.turnPlayer.mv1)

        elif response.lower() == self.turnPlayer.mv2['name']:
            self.turnPlayer.useMv(self.notTurnPlayer, self.turnPlayer.mv2)

        elif response.lower() == self.turnPlayer.mv3['name']:
            self.turnPlayer.useMv(self.notTurnPlayer, self.turnPlayer.mv3)

        elif response.lower() == self.turnPlayer.mv4['name']:
            self.turnPlayer.useMv(self.notTurnPlayer, self.turnPlayer.mv4)

        elif response.lower() == "switch":
            self.__handleSwitch()

        else:
            print("That isn't a valid move, please select a valid move")
            self.__chooseMove()


    def __whatTurnIsIt(self):
        if self.turnPlayer == self.pokemonList1.currentParty[0]:
            print("Player 1")
        elif self.turnPlayer == self.pokemonList2.currentParty[0]:
            print("Player 2")
        if len(self.turnPlayer.types) > 1:
            print("Turn " + str(self.turnCount) + " - " + self.turnPlayer.name.capitalize() + " | Type: " + self.turnPlayer.types[0].capitalize() + " " + self.turnPlayer.types[1].capitalize())
        else:
            print("Turn " + str(self.turnCount) + " - " + self.turnPlayer.name.capitalize() + " | Type: " + self.turnPlayer.types[0].capitalize())
        if len(self.notTurnPlayer.types) > 1:
            print("Opponent" + " - " + self.notTurnPlayer.name.capitalize() + " | Type: " + self.notTurnPlayer.types[0].capitalize() + " " + self.notTurnPlayer.types[1].capitalize())
        else:
            print("Opponent" + " - " + self.notTurnPlayer.name.capitalize() + " | Type: " + self.notTurnPlayer.types[0].capitalize())
        self.__incrementTurnCount()


    def __handleSwitch(self):
        if self.turnPlayer in self.pokemonList1.currentParty:
            self.pokemonList1.printCurrentParty(self.turnPlayer)
            response = input("Please choose from one of your available pokemon: ")
            for pokemon in self.pokemonList1.currentParty:
                if pokemon.name.lower() == response.lower():
                    self.pokemonList1.switchActivePokemon(pokemon)
                    self.turnPlayer = self.pokemonList1.currentParty[0]
                    break
            else:
                print("That is not a valid pokemon, please try again: ")
                self.__handleSwitch()

        elif self.turnPlayer in self.pokemonList2.currentParty:
            self.pokemonList2.printCurrentParty(self.turnPlayer)
            response = input("Please choose from one of your available pokemon: ")
            for pokemon in self.pokemonList2.currentParty:
                if pokemon.name.lower() == response.lower():
                    self.pokemonList2.switchActivePokemon(pokemon)
                    self.turnPlayer = self.pokemonList2.currentParty[0]
                    break
            else:
                print("That is not a valid pokemon, please try again: ")
                self.__handleSwitch()


    def turnPlayerMove(self):
        self.__whatTurnIsIt()
        self.__chooseMove()
        self.__checkHP()
        self.__changeTurnPlayer()
        print("---------------------------------------------------------------")


    def __handleVictory(self, winner):
        print("Player " + winner + " wins the battle!")
        print("---------------------------------------------------------------")
        sys.exit()
