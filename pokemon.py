import requests
import random


class Pokemon:
    def __init__(self):
        pokemon = get_random_pokemon()
        self.name = pokemon["name"].capitalize()
        self.type = pokemon["type"].capitalize()
        self.image = pokemon["image"]
        self.color = get_pokemon_type_color(pokemon["type"])


# Generate some random Pokemon using pokeAPI
def get_random_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/{}".format(random.randint(1, 898))
    response = requests.get(url).json()

    pokemon = {
        "name": response["name"],
        "image": response["sprites"]["other"]["official-artwork"]["front_default"],
        "type": response["types"][0]["type"]["name"],
    }

    return pokemon


def get_pokemon_type_color(type):
    colors = {
        "normal": 0xA8A878,
        "fire": 0xF08030,
        "water": 0x6890F0,
        "electric": 0xF8D030,
        "grass": 0x78C850,
        "ice": 0x98D8D8,
        "fighting": 0xC03028,
        "poison": 0xA040A0,
        "ground": 0xE0C068,
        "flying": 0xA890F0,
        "psychic": 0xF85888,
        "bug": 0xA8B820,
        "rock": 0xB8A038,
        "ghost": 0x705898,
        "dragon": 0x7038F8,
        "dark": 0x705848,
        "steel": 0xB8B8D0,
        "fairy": 0xEE99AC,
    }

    if type in colors:
        return colors[type]
    else:
        return 0x000000
