
class Pokemon:
    def __init__(self, pokemon):
        self.name = pokemon['name']
        self.hp = 100
        self.mv1 = pokemon['moves']['mv1']
        self.mv2 = pokemon['moves']['mv2']
        self.mv3 = pokemon['moves']['mv3']
        self.mv4 = pokemon['moves']['mv4']
        self.types = pokemon['types']
        self.available = True
        self.typeMatchupRefObj = {
            "fire": {
                "normal": 1,
                "fighting": 1,
                "flying": 1,
                "poison": 1,
                "ground": 1,
                "rock": 0.5,
                "bug:": 2,
                "ghost": 1,
                "steel": 2,
                "fire": 0.5,
                "water": 0.5,
                "grass": 2,
                "electric": 1,
                "psychic": 1,
                "ice": 2,
                "dragon": 0.5,
                "dark": 1,
                "fairy": 1
            },
            "normal": {
                "normal": 1,
                "fighting": 1,
                "flying": 1,
                "poison": 1,
                "ground": 1,
                "rock": 0.5,
                "bug": 1,
                "ghost": 0,
                "steel": 0.5,
                "fire": 1,
                "water": 1,
                "grass": 1,
                "electric": 1,
                "psychic": 1,
                "ice": 1,
                "dragon": 1,
                "dark": 1,
                "fairy": 1
            },
            "fighting": {
                "normal": 2,
                "fighting": 1,
                "flying": 0.5,
                "poison": 0.5,
                "ground": 1,
                "rock": 2,
                "bug": 0.5,
                "ghost": 0,
                "steel": 2,
                "fire": 1,
                "water": 1,
                "grass": 1,
                "electric": 1,
                "psychic": 0.5,
                "ice": 2,
                "dragon": 1,
                "dark": 2,
                "fairy": 0.5
            },
            "flying": {
                "normal": 1,
                "fighting": 2,
                'flying': 1,
                'poison': 1,
                'ground': 1,
                'rock': 0.5,
                'bug': 2,
                'ghost': 1,
                'steel': 0.5,
                'fire': 1,
                'water': 1,
                'grass': 2,
                'electric': 0.5,
                'psychic': 1,
                'ice': 1,
                'dragon': 1,
                'dark': 1,
                'fairy': 1
            },
            "poison": {
                "normal": 1,
                "fighting": 1,
                "flying": 1,
                "poison": 0.5,
                "ground": 0.5,
                "rock": 0.5,
                "bug": 1,
                "ghost": 0.5,
                "steel": 0,
                "fire": 1,
                "water": 1,
                "grass": 2,
                "electric": 1,
                "psychic": 1,
                "ice": 1,
                "dragon": 1,
                "dark": 1,
                "fairy": 2
            },
            "ground": {
                "normal": 1,
                "fighting": 1,
                "flying": 0,
                "poison": 2,
                "ground": 1,
                "rock": 2,
                "bug": 0.5,
                "ghost": 1,
                "steel": 2,
                "fire": 2,
                "water": 1,
                "grass": 0.5,
                "electric": 2,
                "psychic": 1,
                "ice": 1,
                "dragon": 1,
                "dark": 1,
                "fairy": 1
            },
            "rock": {
                "normal": 1,
                "fighting": 0.5,
                "flying": 2,
                "poison": 1,
                "ground": 0.5,
                "rock": 1,
                "bug": 2,
                "ghost": 1,
                "steel": 0.5,
                "fire": 2,
                "water": 1,
                "grass": 1,
                "electric": 1,
                "psychic": 1,
                "ice": 2,
                "dragon": 1,
                "dark": 1,
                "fairy": 1
            },
            "bug": {
                "normal": 1,
                "fighting": 0.5,
                "flying": 0.5,
                "poison": 0.5,
                "ground": 1,
                "rock": 1,
                "bug": 1,
                "ghost": 0.5,
                "steel": 0.5,
                "fire": 0.5,
                "water": 1,
                "grass": 2,
                "electric": 1,
                "psychic": 2,
                "ice": 1,
                "dragon": 1,
                "dark": 2,
                "fairy": 0.5
            },
            "ghost": {
                "normal": 0,
                "fighting": 1,
                "flying": 1,
                "poison": 1,
                "ground": 1,
                "rock": 1,
                "bug": 1,
                "ghost": 2,
                "steel": 1,
                "fire": 1,
                "water": 1,
                "grass": 1,
                "electric": 1,
                "psychic": 2,
                "ice": 1,
                "dragon": 1,
                "dark": 0.5,
                "fairy": 1
            },
            "steel": {
                "normal": 1,
                "fighting": 1,
                "flying": 1,
                "poison": 1,
                "ground": 1,
                "rock": 2,
                "bug": 1,
                "ghost": 1,
                "steel": 0.5,
                "fire": 0.5,
                "water": 0.5,
                "grass": 1,
                "electric": 1,
                "psychic": 1,
                "ice": 2,
                "dragon": 1,
                "dark": 1,
                "fairy": 2
            },
            "water": {
                "normal": 1,
                "fighting": 1,
                "flying": 1,
                "poison": 1,
                "ground": 2,
                "rock": 2,
                "bug": 1,
                "ghost": 1,
                "steel": 1,
                "fire": 2,
                "water": 0.5,
                "grass": 0.5,
                "electric": 1,
                "psychic": 1,
                "ice": 1,
                "dragon": 0.5,
                "dark": 1,
                "fairy": 1
            },
            "grass": {
                "normal": 1,
                "fighting": 1,
                "flying": 0.5,
                "poison": 0.5,
                "ground": 2,
                "rock": 2,
                "bug": 0.5,
                "ghost": 1,
                "steel": 0.5,
                "fire": 0.5,
                "water": 2,
                "grass": 0.5,
                "electric": 1,
                "psychic": 1,
                "ice": 1,
                "dragon": 0.5,
                "dark": 1,
                "fairy": 1
            },
            "electric": {
                "normal": 1,
                "fighting": 1,
                "flying": 0.5,
                "poison": 0.5,
                "ground": 0,
                "rock": 1,
                "bug": 1,
                "ghost": 1,
                "steel": 1,
                "fire": 1,
                "water": 2,
                "grass": 0.5,
                "electric": 0.5,
                "psychic": 1,
                "ice": 1,
                "dragon": 0.5,
                "dark": 1,
                "fairy": 1
            },
            "psychic": {
                "normal": 1,
                "fighting": 2,
                "flying": 1,
                "poison": 2,
                "ground": 1,
                "rock": 1,
                "bug": 1,
                "ghost": 1,
                "steel": 0.5,
                "fire": 1,
                "water": 1,
                "grass": 1,
                "electric": 1,
                "psychic": 0.5,
                "ice": 1,
                "dragon": 1,
                "dark": 0,
                "fairy": 1
            },
            "ice": {
                "normal": 1,
                "fighting": 1,
                "flying": 2,
                "poison": 1,
                "ground": 2,
                "rock": 1,
                "bug": 1,
                "ghost": 1,
                "steel": 0.5,
                "fire": 0.5,
                "water": 0.5,
                "grass": 2,
                "electric": 1,
                "psychic": 1,
                "ice": 0.5,
                "dragon": 2,
                "dark": 1,
                "fairy": 1
            },
            "dragon": {
                "normal": 1,
                "fighting": 1,
                "flying": 1,
                "poison": 1,
                "ground": 1,
                "rock": 1,
                "bug": 1,
                "ghost": 1,
                "steel": 0.5,
                "fire": 1,
                "water": 1,
                "grass": 1,
                "electric": 1,
                "psychic": 1,
                "ice": 1,
                "dragon": 2,
                "dark": 1,
                "fairy": 0
            },
            "dark": {
                "normal": 1,
                "fighting": 0.5,
                "flying": 0.5,
                "poison": 1,
                "ground": 1,
                "rock": 1,
                "bug": 1,
                "ghost": 2,
                "steel": 1,
                "fire": 1,
                "water": 1,
                "grass": 1,
                "electric": 1,
                "psychic": 2,
                "ice": 1,
                "dragon": 1,
                "dark": 0.5,
                "fairy": 0.5
            },
            "fairy": {
                "normal": 1,
                "fighting": 2,
                "flying": 1,
                "poison": 0.5,
                "ground": 1,
                "rock": 1,
                "bug": 1,
                "ghost": 1,
                "steel": 0.5,
                "fire": 0.5,
                "water": 1,
                "grass": 1,
                "electric": 1,
                "psychic": 1,
                "ice": 1,
                "dragon": 2,
                "dark": 2,
                "fairy": 1
            }
        }
        self.listOfCreatedpokemon = []


    def __printHP(self, opponent):
        strToConcat = ""
        for _ in range(0, int(opponent.hp / 10)):
            strToConcat = strToConcat + "=="
        print("|" + strToConcat + "|")
        print(str(int(opponent.hp)) + "%")


    def __handleDamage(self, opponent, chosenMv):
        if len(opponent.types) > 1:
            multiplier = self.typeMatchupRefObj[chosenMv['type']][opponent.types[0]] * self.typeMatchupRefObj[chosenMv['type']][opponent.types[1]]
            self.__printEffectivess(multiplier)
            totalDamage = chosenMv['damage'] * multiplier
            opponent.hp -= totalDamage
            return int(totalDamage)
        else:
            multiplier = self.typeMatchupRefObj[chosenMv['type']][opponent.types[0]]
            self.__printEffectivess(multiplier)
            totalDamage = chosenMv['damage'] * multiplier
            opponent.hp -= totalDamage
            return int(totalDamage)


    def __printEffectivess(self, multiplier):
        if multiplier == 2:
            print("It was super-effective!")
        elif multiplier == 0.5:
            print("It wasn't very effective...")
        elif multiplier == 0:
            print("It didn't seem to affect it at all!")


    def useMv(self, opponent, chosenMv):
        print(self.name + " used " + chosenMv['name'] + "!")
        totalDamage = self.__handleDamage(opponent, chosenMv)
        print(opponent.name + " took " + str(totalDamage) + " damage!")
        if opponent.hp > 0:
            print(str(opponent.name) + " HP:")
            self.__printHP(opponent)
