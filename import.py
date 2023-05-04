import sqlite3
# import sys
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# result = pokemonColl.delete_many({})

connection = sqlite3.connect('pokemon.sqlite')
pokemonCursor = connection.cursor()
pokemon_data = pokemonCursor.execute(
    "SELECT p.name, p.pokedex_number, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense FROM pokemon p").fetchall()

for poke in pokemon_data:
    ability_lst = []
    abilities = pokemonCursor.execute(
        "SELECT a.name FROM ability a JOIN pokemon_abilities p ON a.id = p.ability_id WHERE p.pokemon_id=?", (poke[1],)).fetchall()
    for ability in abilities:
        new = ability[0].strip("',")
        ability_lst.append(new)
    types_lst = []
    types = pokemonCursor.execute(
        "SELECT type1, type2 FROM pokemon_types_view p WHERE p.name=?", (poke[0],)).fetchall()

    pokemon_object = {
        "name": poke[0],
        "pokedex_number": poke[1],
        "types": [types[0][0], types[0][1]],
        "hp": poke[2],
        "attack": poke[3],
        "defense": poke[4],
        "speed": poke[5],
        "sp_attack": poke[6],
        "sp_defense": poke[7],
        "abilities": ability_lst
    }
    pokemonColl.insert_one(pokemon_object)

cursor = pokemonColl.find({})

for document in cursor:
    print(document)
