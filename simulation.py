import requests
import json
import random 
import sys

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.hp=None
        self.base_stat_attack=None 
        self.base_stat_defense=None
        self.moves=[]
        self.getPokeData()

    #function to get data from the PokeApi
    def getPokeData(self):
        try:
            r = requests.get("https://pokeapi.co/api/v2/pokemon/" + self.name)
            r.raise_for_status()
            response=r.json()

            # base stats
            self.hp = response["stats"][0]["base_stat"]
            self.base_stat_attack = response["stats"][1]["base_stat"]
            self.base_stat_defense = response["stats"][2]["base_stat"]
            for move in response["moves"]:
                self.moves.append(move["move"])
        except requests.exceptions.HTTPError as err:
            print("pokemon data not found")
            raise SystemExit(err)
    # get : returns the base_stats_attack
    def getBaseStatsAttack(self):
        return self.base_stat_attack
    
    # get : returns the base_stats_defense
    def getBaseStatsDefense(self):
        return self.base_stat_defense
    
    # get : returns the name
    def getName(self):
        return self.name

    # get : returns the hp
    def getHp(self):
        return self.hp

    # inflict damage on the pokemon
    def inflictDamage(self,damage):
        self.hp=round(self.hp-damage,3)
    
    # get : generates a random number between 0 and length of moves
    def getMoveIndex(self):
        return random.randint(0, len(self.moves) - 1)
    
    def print(self):
        print("name : " + self.name)
        print("hp : " + str(self.hp))
        print("attack : " + str(self.base_stat_attack))
        print("defense : " + str(self.base_stat_defense))
        print("--------------------------------------------")
        #print(self.moves)

class Move:
    def __init__(self,index,source_poke,destination_poke):
        self.move_name=source_poke.moves[index]["name"]
        self.move_url=source_poke.moves[index]["url"]
        self.move_power=None 
        self.move_damage=None
        self.getMoveData(source_poke,destination_poke)

    #function to get move data from the PokeApi
    def getMoveData(self,source_poke,destination_poke):
        try:
            r = requests.get(self.move_url)
            r.raise_for_status()
            response=r.json()

            #get move power and pp
            self.move_power=response["power"]
            self.move_pp=response["pp"]
            if(self.move_power)==None:
                self.move_power=31
            if(self.move_pp)==None:
                self.move_pp=20

            # damage inflicted on the opponent
            attack=source_poke.getBaseStatsAttack()
            defense=destination_poke.getBaseStatsDefense()
            self.move_damage=((2 * self.move_power * attack) / defense) / 50 + 2
            self.move_damage=round(self.move_damage,3)
            destination_poke.inflictDamage(self.move_damage)
            self.showMoveResults(source_poke,destination_poke)

        except requests.exceptions.HTTPError as err:
            print("move data not found")
            raise SystemExit(err)
    
    def showMoveResults(self,source_poke,destination_poke):
        print(source_poke.getName()+" attacks "+destination_poke.getName())
        print("move : "+str(self.move_name))
        print("power : "+str(self.move_power))
        print("damage inflicted on "+destination_poke.getName()+" : "+str(self.move_damage))
        print(source_poke.getName()+"'s hp :"+str(source_poke.getHp()))
        print(destination_poke.getName()+"'s hp :"+str(destination_poke.getHp()))
        print("-------------------------------------------")

    def print(self):
        print("name : " + self.move_name)
        print("url : "+self.move_url)
        print("power : " + str(self.move_power))
        print("damage : " + str(self.move_damage))
        print("--------------------------------------------")
        #print(self.moves)

# simulates a battle between two pokemons
def battleBetweenTwoPokemons(playerA,playerB):
    isFirst=True
    while(playerA.getHp()>0 and playerB.getHp()>0):
        if isFirst:
            move=Move(playerA.getMoveIndex(),playerA,playerB)
        else:
            move=Move(playerB.getMoveIndex(),playerB,playerA)
        isFirst=not isFirst
    
    if playerA.getHp()>playerB.getHp():
        # print(playerA.getName()+" wins")
        return {'winner':playerA.getName(),'loser':playerB.getName()}
    else:
        # print(playerB.getName()+" wins")
        return {'winner':playerB.getName(),'loser':playerA.getName()}

def startBattle(pokemonName1,pokemonName2):
    playerA=Pokemon(pokemonName1)
    playerB=Pokemon(pokemonName2)
    result=battleBetweenTwoPokemons(playerA,playerB)
    print(result['winner']+" has won")

def startTeamBattle(teamA,teamB):
    random.shuffle(teamA)
    random.shuffle(teamB)
    listA=[]
    listB=[]

    # filling team info using the team names
    for ta in teamA:
        teamItem=Pokemon(ta)
        listA.append(teamItem)
    for tb in teamB:
        teamItem=Pokemon(tb)
        listB.append(teamItem)

    # battle
    while(len(listA)>0 and len(listB)>0):
        min_size=min(len(listA),len(listB))
        for i in range(0,min_size):
            result=battleBetweenTwoPokemons(listA[i],listB[i])
            if listA[i].getName()==result['loser']:
                listA.remove(listA[i])
                break
            else:
                listB.remove(listB[i])
                break
    # showing the remaining heroes 
    if len(listA)>0:
        print("team B has no pokemons left")
        print("team A has won")
        print("team A members still alive ",end="")
        print("[ ",end='')
        for t in listA:
            print(t.getName(),end=' ')
        print("]",end='')
    else:
        print("team A has no pokemons left")
        print("team B has won")
        print("team B members still alive ",end="")
        print("[ ",end='')
        for t in listB:
            print(t.getName(),end=' ')
        print("]",end='')
