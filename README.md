# Category: senior
I've been writing code for about 36 months

## PokeArena : Create your own dream team and battle it out!

A Pokemon battle simulator that lets you battle Pokémon against each other using the data from the PokeAPI. 
- You can battle any two Pokemon against each other that are in the PokeAPI database
- You can create teams  of Pokemons and battle other trainers' teams, the first trainer to have all of their Pokemon faint loses the battle.

## Prerequisites
* python3
* internet<br/>
##### The code solely relies on built-in modules.<br /><br />

## Quick start

The code was tested on servers running Debian GNU/Linux and will work correctly on any clean system.
Use the following commands to get started:

```sh
$ git clone https://github.com/brianzhou139/PokeArena.git
$ cd PokeArena
```
### Simulating a battle between two pokemons
To simulate a battle between two pokemons of choice, launch the app using the following parameters:

```sh
$ python3 main.py -b <pokemon1_name> <pokemon2_name>
```
where: 
<pokemon1_name> – name of pokemon e.g bulbasaur,
<pokemon2_name> – name of pokemon e.g charizard.

#### Example 
```sh
$ python3 main.py -b bulbasaur charizard
```

### Simulating a battle between two teams
To simulate a battle between two teams, launch the app using the following parameters:

```sh
$ python3 main.py -b <first_team_file> <second_team_file>
```
where:<br/>
<first_team_file> – path to the text file containing the names of the members of the first team e.g teamA.txt <br/>
<second_team_file> – path to the text file containing the names of the members of the second teame.g teamB.txt.

Each file must contain a list of team members separated by commas, spaces, or newlines.

#### Example 
```sh
$ python3 main.py -b teamA.txt teamB.txt
```

The output data is displayed as text on the console, which shows the results of the moves played by the pokemons, as well as the overall outcome of the battle.<br/>
#### Sample output : 
```sh
...
...
charizard attacks kakuna
move : natural-gift
power : 31
damage inflicted on kakuna : 4.083
charizard's hp :65.399
kakuna's hp :3.634
-------------------------------------------
kakuna attacks charizard
move : electroweb
power : 55
damage inflicted on charizard : 2.705
kakuna's hp :3.634
charizard's hp :62.694
-------------------------------------------
charizard attacks kakuna
move : power-up-punch
power : 40
damage inflicted on kakuna : 4.688
charizard's hp :62.694
kakuna's hp :-1.054
-------------------------------------------
charizard has won
```
