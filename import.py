import sqlite3
import sys
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

connection = sqlite3.connect('pokemon.sqlite')
pokemonCursor = connection.cursor()
pokemon_data = pokemonCursor.execute(
    "SELECT p.name, p.pokedex_number, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, (t2.type1 || ' ' || t2.type2) AS types FROM pokemon AS p JOIN pokemon_types_view AS t2 ON p.name = t2.name").fetchall()

for poke in pokemon_data:
    ability_lst = []
    abilities = pokemonCursor.execute(
        "SELECT a.name FROM ability a JOIN pokemon_abilities p ON a.id = p.ability_id WHERE p.pokemon_id=?", (poke[1],)).fetchall()
    for ability in abilities:
        new = ability[0].strip("',")
        ability_lst.append(new)
    pokemon_object = {
        "name": poke[0],
        "pokedex_number": poke[1],
        "types": [poke[8]],
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
