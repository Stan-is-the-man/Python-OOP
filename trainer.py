class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for every_pokemon in self.pokemons:
            if every_pokemon.name == pokemon_name:
                self.pokemons.remove(every_pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"
        return result



