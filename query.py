from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

query = {"name": "Pikachu"}

pikachu = pokemonColl.find(query)
for val in pikachu:
    print(val)
above_150 = pokemonColl.find({"attack": {"$gt": 150}})
for above in above_150:
    print(above)
# overgrow = pokemonColl.find({"abilities": {"$elemMatch": {"$eq": "Overgrow"}}})
# for pokemon_obj in overgrow:
#     print(pokemon_obj)
