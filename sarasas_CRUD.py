def print_info():
    print('-----------------------------------------------------------------------')
    print('1. Atvaizduoti filmu pasirinkimus')
    print('2. Itraukti filmus i sarasa')
    print('3. Redaguoti filmus')
    print('4. Pasalinti filmus')
    print('5. Iseiti is programos')
    print('-----------------------------Pasirinkite--------------------------------')

def print_films(films):
    for flm in films:
        print(f'{flm['id']}. Filmas \"{flm['title']}\", kuri sukure {flm['director']} ir isleido {flm['release_year']} metais')

def create_film(films, id_counter):
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
        'release_year': release_year}
    print(f'{flm['id']}. Itraukta: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')

    films.append(flm)
    return id_counter

def edit_film(films):
    print('Filmu redagavimas')
    print('iveskite filmo id, kuri norite redaguoti')
    edit_id = input()
    for flm in films:
        if edit_id == str(flm['id']):
            print(
                f'{flm['id']}. Redaguojama: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')
            print('iveskite filmo pavadinima')
            flm['title'] = input()
            print('iveskite filmo autoriu')
            flm['director'] = input()
            print('iveskite filmo isleidimo metus')
            flm['release_year'] = int(input())
            print(f'{flm['id']}. Pakeista i: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')

            break

def delete_film(films):
    print('Filmu pasalinimas')
    print('iveskite filmo id, kuri norite pasalinti')
    del_id = input()
    for flm in films:
        if del_id == str(flm['id']):
            print(f'{flm['id']}. Pasalinta: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')
            films.remove(flm)
            break