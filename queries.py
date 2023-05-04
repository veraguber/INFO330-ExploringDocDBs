pikachu = pokemonColl.find({"name": "Pikachu"})
above_150 = pokemonColl.find({"attack": {"$gt": 150}})
overgrow = pokemonColl.find()
