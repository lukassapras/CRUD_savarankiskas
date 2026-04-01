import mysql.connector

DB_CONFIG = {
    'host':'localhost', #127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3306,
    'user':'root',
    'password':"Root123.",
    'database':'filmai'
}
headers = ['id', 'title', 'director', 'release_year']

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_films():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from filmai')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    films_list = []
    for row in rows:
        single_film = {}
        for col_num in range(len(headers)):
            single_film[headers[col_num]] = str(row[col_num]).replace('\r','')
        films_list.append(single_film)
    return films_list

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
    print('Filmu itraukimas')
    print('iveskite pavadinima')
    title = input()
    print('iveskite autoriu')
    director = input()
    print('iveskite isleidimo metus')
    release_year = int(input())
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO `filmai` (`title`,`director`,`release_year`)VALUES(%s,%s,%s);',
                (title, director, release_year))
    conn.commit()
    cur.close()
    conn.close()

def edit_film():
    print('Filmu redagavimas')
    print('iveskite filmo id, kuri norite redaguoti')
    edit_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from filmai where id = %s', (edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        print(f'{row[0]}. Redaguojama: \"{row[1]}\", filmo autorius {row[2]}, isleidimo metai: {row[3]}')
        print('iveskite filmo pavadinima')
        title = input()
        print('iveskite filmo autoriu')
        director = input()
        print('iveskite filmo isleidimo metus')
        release_year = int(input())
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('UPDATE `filmai` SET `title` = %s,`director` = %s,'
                    '`release_year` = %s WHERE `id` = %s;', (title, director, release_year, edit_id))
        conn.commit()
        cur.close()
        conn.close()
        print(f'{row[0]}. Pakeista i: \"{row[1]}\", filmo autorius {row[2]}, isleidimo metai: {row[3]}')
    else:
        print('tokio iraso nera')

def delete_film():
    print('Filmu pasalinimas')
    print('iveskite filmo id, kuri norite pasalinti')
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from filmai where id = %s', (del_id,))
    row = cur.fetchone()
    if row:
        print(f'{row[0]}. Pasalinta: \"{row[1]}\", filmo autorius {row[2]}, isleidimo metai: {row[3]}')
        cur.execute('delete from filmai where id = %s',(del_id,))
        conn.commit()
    else:
        print('tokio iraso nera')
    cur.close()
    conn.close()