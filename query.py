from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

pikachu = pokemonColl.find({'name': 'Pikachu'})
for val in pikachu:
    print(val)
# above_150 = pokemonColl.find({"attack": {"$gt": 150}})
# print(above_150)
# overgrow = pokemonColl.find({"abilities": {"$elemMatch": {"$eq": "Overgrow"}}})
# print(overgrow)
