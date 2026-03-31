from demo_data import load_films
from sarasas_CRUD import *

films = load_films()
id_counter = 3

while True:
    print_info()
    pasirinkimas = input()
    match pasirinkimas:
        case '1':
            print_films(films)
        case '2':
            id_counter = create_film(films, id_counter)
        case '3':
            edit_film(films)
        case '4':
            delete_film(films)
        case '5':
            print('GEROS KLOTIES')
            break