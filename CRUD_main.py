films = [
    {
        'id': 1,
          'title': 'Filmu dinastija',
          'director': 'Lukas Mickus',
          'release_year': 2026
    },
    {
        'id': 2,
          'title': 'Pythono agonija',
          'director': 'Naglis Mockevičius',
          'release_year': 2013
    },
    {
        'id': 3,
          'title': 'Nerandu ka apsirengti',
          'director': 'Jūratė Pečkaitienė',
          'release_year': 2024
    }
]
id_counter = 3

while True:
    print('-----------------------------------------------------------------------')
    print('1. Atvaizduoti filmu pasirinkimus')
    print('2. Itraukti filmus i sarasa')
    print('3. Redaguoti filmus')
    print('4. Istrinti filmus')
    print('5. Iseiti is programos')
    print('-----------------------------Pasirinkite--------------------------------')
    pasirinkimas = input()
    match pasirinkimas:

        case '1':
            for flm in films:
                print(f'{flm['id']}. Filmas \"{flm['title']}\", kuri sukure {flm['director']} ir isleido {flm['release_year']} metais')

        case '2':
            print('Filmu itraukimas')
            print('iveskite pavadinima')
            title = input()
            print('iveskite autoriu')
            director = input()
            print('iveskite isleidimo metus')
            release_year = int(input())
            id_counter += 1
            flm = {
                'id': id_counter,
                'title': title,
                'director': director,
                'release_year': release_year
            }
            films.append(flm)

        case '3':
            print('Filmu redagavimas')
            print('iveskite filmo id, kuri norite redaguoti')
            edit_id = input()
            for flm in films:
                if edit_id == str(flm['id']):
                    print(f'{flm['id']}. Redaguojama: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')
                    print('iveskite filmo pavadinima')
                    flm['title'] = input()
                    print('iveskite filmo autoriu')
                    flm['director'] = input()
                    print('iveskite filmo isleidimo metus')
                    flm['release_year'] = int(input())
                    break

        case '4':
            print('Filmu pasalinimas')
            print('iveskite filmo id, kuri norite pasalinti')
            del_id = input()
            for flm in films:
                if del_id == str(flm['id']):
                    print(f'{flm['id']}. Pasalinta: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')
                    films.remove(flm)

        case '5':
            print('GEROS KLOTIES')
            break