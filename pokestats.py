import sys
import requests


def main():
    try:
        pokemon_name = sys.argv[1]
        get_stats(pokemon_name)
    except IndexError:
        print("Gotta catch 'em all! Please choose a Pokemon name!")
        print('Example:\n\tpython pokestats.py bulbasaur')


def get_stats(pokemon_name=None, pokeapi=None):
    if pokeapi is None:
        pokeapi = 'http://pokeapi.co/api/v2/'

    pokemon_data = requests.get(pokeapi + 'pokemon/' + pokemon_name.lower())

    if pokemon_data.status_code == 200:
        stats = pokemon_data.json()['stats']
        print_stats(pokemon_name, stats)
    else:
        print('Stats are not available for', pokemon_name)


def print_stats(pokemon_name=None, pokemon_stats={}):
    print('******************************************************************')
    print('Stats for', pokemon_name)
    print('******************************************************************')

    for stat in pokemon_stats:
        print(stat['stat']['name'])
        print('\tbase:', stat['base_stat'])
        print('\teffort:', stat['effort'])


if __name__ == '__main__':
    main()
