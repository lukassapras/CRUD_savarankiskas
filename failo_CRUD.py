import csv

headers = ['id', 'title', 'director', 'release_year']
def load_films():
    with open('films.csv', mode='r', encoding='utf-8')as file:
        return list(csv.DictReader(file))

def save_films(films):
    with open('./films.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(films)

def print_info():
    print('-----------------------------------------------------------------------')
    print('1. Atvaizduoti filmu pasirinkimus')
    print('2. Itraukti filmus i sarasa')
    print('3. Redaguoti filmus')
    print('4. Pasalinti filmus')
    print('5. Iseiti is programos')
    print('-----------------------------Pasirinkite--------------------------------')

def print_films():
    films = load_films()
    for flm in films:
        print(f'{flm['id']}. Filmas \"{flm['title']}\", kuri sukure {flm['director']} ir isleido {flm['release_year']} metais')

def create_film():
    films = load_films()
    print('Filmu itraukimas')
    print('iveskite pavadinima')
    title = input()
    print('iveskite autoriu')
    director = input()
    print('iveskite isleidimo metus')
    release_year = int(input())
    id_counter = int(films[-1]['id']) + 1 if len(films) > 0 else 1
    flm = {
        'id': id_counter,
        'title': title,
        'director': director,
        'release_year': release_year}
    print(f'{flm['id']}. Itraukta: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')
    films.append(flm)
    save_films(films)

def edit_film():
    films = load_films()
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
            print(f'{flm['id']}. Pakeista i: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')
            break
    save_films(films)

def delete_film():
    films = load_films()
    print('Filmu pasalinimas')
    print('iveskite filmo id, kuri norite pasalinti')
    del_id = input()
    for flm in films:
        if del_id == str(flm['id']):
            print(f'{flm['id']}. Pasalinta: \"{flm['title']}\", filmo autorius {flm['director']}, isleidimo metai: {flm['release_year']}')
            films.remove(flm)
            break
    save_films(films)