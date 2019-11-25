import sqlite3
from config import database
from datetime import datetime

debug = True


def check_tables_exists():

    tables_required = ['heroes', 'matches', 'items']
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT COUNT(*)
    FROM sqlite_master
    WHERE type = ? AND name = ?

    '''

    for table_name in tables_required:
        cursor.execute(SQLQuery,
                       ('table', table_name))

        if cursor.fetchone()[0] == 1:
            if debug:
                print('The table named {} exists'.format(table_name))
        elif table_name == 'heroes':
            create_heroes_table()
        elif table_name == 'matches':
            create_matches_table()
        elif table_name == 'items':
            create_items_table()
        else:
            print(table_name)

    cursor.close()
    connection.close()


def create_heroes_table():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    CREATE TABLE heroes (hero_id INTEGER PRIMARY KEY, hero_name TEXT)

    '''

    cursor.execute(SQLQuery)
    cursor.close()
    connection.close()


def check_hero_exists(hero_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT COUNT(*)
    FROM 'heroes'
    WHERE hero_id = :hero_id

    '''

    cursor.execute(SQLQuery, {'hero_id': hero_id})

    if cursor.fetchone()[0] == 1:
        cursor.close()
        if debug:
            print('The hero id {} exists'.format(hero_id))
        connection.close()
        return True

    if debug:
        print('The hero id {} was added'.format(hero_id))

    return False

    cursor.close()
    connection.close()


def add_hero(hero_id, hero_name):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    INSERT INTO heroes VALUES(?, ?)

    '''

    cursor.execute(SQLQuery, (hero_id, hero_name))

    connection.commit()
    cursor.close()
    connection.close()


def create_matches_table():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''
    CREATE TABLE matches (
    match_number INTEGER PRIMARY KEY,
    match_id INTEGER,
    game_mode INTEGER,
    radiant_win INTEGER,
    dire_team INTEGER,
    hero_id INTEGER,
    hero_level INTEGER,
    kills INTEGER,
    deaths INTEGER,
    assists INTEGER,
    last_hits INTEGER,
    denies INTEGER,
    gold_per_min INTEGER,
    xp_per_min INTEGER,
    hero_damage INTEGER,
    tower_damage INTEGER,
    hero_healing INTEGER,
    remaining_gold INTEGER,
    gold_spent INTEGER,
    item_list TEXT,
    backpack_list TEXT,
    hero_abilities TEXT,
    first_blood_time INTEGER,
    match_duration INTEGER,
    match_seq_num INTEGER,
    leaver_status INTEGER,
    match_date_time timestamp,
    inserted_date_time timestamp
    )'''

    cursor.execute(SQLQuery)
    cursor.close()
    connection.close()


def check_match_exists(match_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT COUNT(*)
    FROM 'matches'
    WHERE match_id = :match_id

    '''

    cursor.execute(SQLQuery, {'match_id': match_id})

    if cursor.fetchone()[0] == 1:
        cursor.close()
        if debug:
            print('The match id {} exists'.format(match_id))
        connection.close()
        return True

    if debug:
        print('The match id {} does not exists'.format(match_id))

    return False

    cursor.close()
    connection.close()


def add_match(match_id, game_mode, radiant_win, dire_team, hero_id,
              hero_level, kills, deaths, assists, last_hits, denies,
              gold_per_min, xp_per_min, hero_damage, tower_damage,
              hero_healing, remaining_gold, gold_spent, item_list,
              backpack_list, hero_abilities, first_blood_time, match_duration,
              match_seq_num, leaver_status, match_date_time):

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    INSERT INTO matches(match_id, game_mode, radiant_win, dire_team,
    hero_id, hero_level, kills, deaths, assists, last_hits, denies,
    gold_per_min, xp_per_min, hero_damage, tower_damage, hero_healing,
    remaining_gold, gold_spent, item_list, backpack_list, hero_abilities,
    first_blood_time, match_duration, match_seq_num, leaver_status,
    match_date_time, inserted_date_time)

    VALUES (:match_id, :game_mode, :radiant_win, :dire_team, :hero_id,
    :hero_level, :kills, :deaths, :assists, :last_hits, :denies, :gold_per_min,
    :xp_per_min, :hero_damage, :tower_damage, :hero_healing, :remaining_gold,
    :gold_spent, :item_list, :backpack_list, :hero_abilities,
    :first_blood_time, :match_duration, :match_seq_num, :leaver_status,
    :match_date_time, :inserted_date_time)

    '''

    # Converts the Unix time to human readable date and time
    match_date_time = str(datetime.utcfromtimestamp(match_date_time).strftime
                          ('%Y-%m-%d %H:%M:%S'))

    inserted_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute(SQLQuery, {'match_id': match_id, 'game_mode': game_mode,
                              'radiant_win': radiant_win,
                              'dire_team': dire_team,
                              'hero_id': hero_id,
                              'hero_level': hero_level, 'kills': kills,
                              'deaths': deaths, 'assists': assists,
                              'last_hits': last_hits, 'denies': denies,
                              'gold_per_min': gold_per_min,
                              'xp_per_min': xp_per_min,
                              'hero_damage': hero_damage,
                              'tower_damage': tower_damage,
                              'hero_healing': hero_healing,
                              'remaining_gold': remaining_gold,
                              'gold_spent': gold_spent, 'item_list': item_list,
                              'backpack_list': backpack_list,
                              'hero_abilities': hero_abilities,
                              'first_blood_time': first_blood_time,
                              'match_duration': match_duration,
                              'match_seq_num': match_seq_num,
                              'leaver_status': leaver_status,
                              'match_date_time': match_date_time,
                              'inserted_date_time': inserted_date_time})

    connection.commit()
    cursor.close()
    connection.close()

def create_items_table():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''
    CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT,
    item_cost INTEGER,
    item_secret_shop INTEGER,
    item_side_shop INTEGER,
    item_recipe INTEGER
    )'''

    cursor.execute(SQLQuery)
    cursor.close()
    connection.close()

def check_item_exists(item_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT COUNT(*)
    FROM 'items'
    WHERE item_id = :item_id

    '''

    cursor.execute(SQLQuery, {'item_id': item_id})

    if cursor.fetchone()[0] == 1:
        cursor.close()
        if debug:
            print('The item id {} exists'.format(item_id))
        connection.close()
        return True

    if debug:
        print('The item id {} does not exists'.format(item_id))

    return False

    cursor.close()
    connection.close()

def add_item(item_id, item_name, item_cost, item_secret_shop,
                item_side_shop, item_recipe):

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    INSERT INTO items(item_id, item_name, item_cost, item_secret_shop,
    item_side_shop, item_recipe)

    VALUES (:item_id, :item_name, :item_cost, :item_secret_shop, 
    :item_side_shop, :item_recipe)

    '''

    cursor.execute(SQLQuery, {'item_id': item_id, 'item_name': item_name,
                                'item_cost': item_cost, 
                                'item_secret_shop': item_secret_shop,
                                'item_side_shop': item_side_shop,
                                'item_recipe': item_recipe})

    connection.commit()
    cursor.close()
    connection.close()

def get_latest_match_id():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT match_id
    FROM 'matches'
    ORDER BY match_date_time DESC
    LIMIT 1

    '''

    cursor.execute(SQLQuery)

    match_id = cursor.fetchone()

    cursor.close()
    connection.close()

    return match_id[0]


def get_latest_number_of_heroes_from_database():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT count(hero_id)
    FROM 'heroes'

    '''

    cursor.execute(SQLQuery)

    number_of_heroes = cursor.fetchone()

    cursor.close()
    connection.close()

    return number_of_heroes[0]

def get_latest_number_of_items_from_database():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT count(item_id)
    FROM 'items'

    '''

    cursor.execute(SQLQuery)

    number_of_items = cursor.fetchone()

    cursor.close()
    connection.close()

    return number_of_items[0]
    
#  LocalWords:  xp
