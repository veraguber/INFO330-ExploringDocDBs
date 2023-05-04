import sqlite3
import sys
from pymongo import MongoClient

# mongoClient = MongoClient("mongodb://localhost/pokemon")
# pokemonDB = mongoClient['pokemondb']
# pokemonColl = pokemonDB['pokemon_data']

connection = sqlite3.connect('pokemon.sqlite')
pokemonCursor = connection.cursor()
pokemon_data = pokemonCursor.execute(
    "SELECT p.name, p.pokedex_number, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, (t2.type1 || ' ' || t2.type2) AS types FROM pokemon AS p JOIN pokemon_types_view AS t2 ON p.name = t2.name LIMIT 10").fetchall()
for pokemon in table_w_types:
    print(pokemon)

# basic_pokemon_info = pokemonCursor.execute(
#     "SELECT name, pokedex_number, hp, attack, defense, speed, sp_attack, sp_defense FROM pokemon LIMIT 10").fetchall()
# for pokemon in basic_pokemon_info:
#     print(pokemon)

for poke in pokemon_data:
    abilities = pokemonCursor.execute(
        "SELECT a.name FROM ability a JOIN pokemon_abilities p ON a.id = p.ability_id WHERE p.pokemon_id=?", (poke[2],)).fetchall()
    pokemon_object = {
        "name": poke[1],
        "pokedex_number": poke[2],
        "types": [poke[9]],
        "hp": poke[3],
        "attack": poke[4],
        "defense": poke[5],
        "speed": poke[6],
        "sp_attack": poke[7],
        "sp_defense": poke[8],
        "abilities": abilities
    }
pokemonColl.insert_one(pokemon_object)
