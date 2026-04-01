from sarasas_CRUD import *

while True:
    print_info()
    pasirinkimas = input()
    match pasirinkimas:
        case '1':
            print_films()
        case '2':
            create_film()
        case '3':
            edit_film()
        case '4':
            delete_film()
        case '5':
            print('GEROS KLOTIES')
            break