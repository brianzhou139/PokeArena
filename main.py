
# argv.py
import sys
from simulation import startBattle
from simulation import startTeamBattle

# retrieving pokemon team members from a text file
def getDataFromFile(file_name):
    result=set()
    # open the data file
    file = open(file_name,"r")
    # read the file as a list
    data = file.readlines()
    # close the file
    file.close()

    # handling the lines 
    for line in data:
        line=line.strip()
        line=line.split(",")
        for word in line:
            word=word.lower()
            result.add(word)
    return list(result)

def main():
    # console args
    s_name=sys.argv[0]
    args=sys.argv[1:]
    mode=args[0]
    nameOrFile1=args[1]
    nameOrFile2=args[2]

    if mode=='-b':
        sz=nameOrFile1.split(".")
        if len(sz)==1:
            nameOrFile1=nameOrFile1.lower()
            nameOrFile2=nameOrFile2.lower()
            # starting battle simulation between two pokemons
            startBattle(nameOrFile1,nameOrFile2)
            
        if len(sz)==2:
            teamA=getDataFromFile(nameOrFile1)
            teamB=getDataFromFile(nameOrFile2)
            # starting battle simulation between two pokemons
            startTeamBattle(teamA,teamB)
            
if __name__ == "__main__":
    main()

