import ast
import sqlite3

database = 'database/database.db'


def get_heroes():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT *
    FROM 'heroes'

    '''

    cursor.execute(SQLQuery)

    heroes_data = cursor.fetchall()

    number_of_heroes = len(heroes_data)

    heroes = {}

    i = 0

    while i < number_of_heroes:
        heroes[str(i)] = {}
        heroes[str(i)]['hero_id'] = heroes_data[i][0]
        heroes[str(i)]['hero_name'] = heroes_data[i][1]
        i += 1

    return heroes


def get_recent_matches(matches_requested, hero_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    if hero_id is None:

        SQLQuery = '''

        SELECT match_id
        FROM 'matches'
        ORDER BY match_date_time DESC
        LIMIT {}

        '''

    else:

        SQLQuery = '''

        SELECT match_id
        FROM 'matches'
        WHERE hero_id = :hero_id
        ORDER BY match_date_time DESC
        LIMIT {}

        '''

    cursor.execute(SQLQuery.format(matches_requested), {'hero_id': hero_id})

    match_data = cursor.fetchall()

    cursor.close()
    connection.close()

    match_ids = []

    for match_id in match_data:
        match_ids.append(match_id)

    return get_match_result(match_ids)


def get_match_result(match_ids):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT *
    FROM 'matches'
    WHERE match_id = :match_id

    '''
    match_data = []

    for match_id in match_ids:
        cursor.execute(SQLQuery, {'match_id': match_id[0]})
        data = cursor.fetchone()
        match_data.append(data)

    cursor.close()
    connection.close()

    matches = {}

    amount_of_matches = len(match_data)
    i = 0

    while(i < amount_of_matches):
        matches[str(i)] = {}

        matches[str(i)]['match_number'] = match_data[i][0]
        matches[str(i)]['match_id'] = match_data[i][1]
        matches[str(i)]['game_mode'] = match_data[i][2]
        matches[str(i)]['radiant_win'] = match_data[i][3]
        matches[str(i)]['dire_team'] = match_data[i][4]
        matches[str(i)]['hero_id'] = match_data[i][5]
        matches[str(i)]['hero_level'] = match_data[i][6]
        matches[str(i)]['kills'] = match_data[i][7]
        matches[str(i)]['deaths'] = match_data[i][8]
        matches[str(i)]['assists'] = match_data[i][9]
        matches[str(i)]['last_hits'] = match_data[i][10]
        matches[str(i)]['denies'] = match_data[i][11]
        matches[str(i)]['gold_per_min'] = match_data[i][12]
        matches[str(i)]['xp_per_min'] = match_data[i][13]
        matches[str(i)]['hero_damage'] = match_data[i][14]
        matches[str(i)]['tower_damage'] = match_data[i][15]
        matches[str(i)]['hero_healing'] = match_data[i][16]
        matches[str(i)]['remaining_gold'] = match_data[i][17]
        matches[str(i)]['gold_spent'] = match_data[i][18]
        matches[str(i)]['items'] = ast.literal_eval(match_data[i][19])
        matches[str(i)]['backpack'] = ast.literal_eval(match_data[i][20])
        matches[str(i)]['hero_abilities'] = ast.literal_eval(match_data[i][21])
        matches[str(i)]['first_blood_time'] = match_data[i][22]
        matches[str(i)]['match_duration'] = match_data[i][23]
        matches[str(i)]['match_seq_num'] = match_data[i][24]
        matches[str(i)]['leaver_status'] = match_data[i][25]
        matches[str(i)]['match_date_time'] = match_data[i][26]
        matches[str(i)]['inserted_date_time'] = match_data[i][27]

        i += 1

    return matches


# TODO convert radian win to win matches percentage
def get_averages_of_latest_matches(matches_requested, hero_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    if hero_id is None:

        SQLQuery = '''
        SELECT
        radiant_win, avg(kills), avg(deaths), avg(assists), avg(last_hits),
        avg(denies), avg(gold_per_min), avg(xp_per_min), avg(hero_damage),
        avg(tower_damage), avg(hero_healing), avg(remaining_gold) +
        avg(gold_spent)
        FROM 'matches'
        LIMIT {}
        '''

    else:

        SQLQuery = '''
        SELECT
        radiant_win, avg(kills), avg(deaths), avg(assists), avg(last_hits),
        avg(denies), avg(gold_per_min), avg(xp_per_min), avg(hero_damage),
        avg(tower_damage), avg(hero_healing), avg(remaining_gold) +
        avg(gold_spent)
        FROM 'matches'
        WHERE hero_id = :hero_id
        LIMIT {}
        '''

    cursor.execute(SQLQuery.format(matches_requested), {'hero_id': hero_id})

    data = cursor.fetchone()

    averages = {}

    averages['average_kills'] = round(data[1])
    averages['average_deaths'] = round(data[2])
    averages['average_assists'] = round(data[3])
    averages['average_last_hits'] = round(data[4])
    averages['average_denies'] = round(data[5])
    averages['average_gold_per_min'] = round(data[6])
    averages['average_xp_per_min'] = round(data[7])
    averages['average_hero_damage'] = round(data[8])
    averages['average_tower_damage'] = round(data[9])
    averages['average_hero_healing'] = round(data[10])
    averages['average_net_worth'] = round(data[11])

    return averages


def get_items():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT *
    FROM items

    '''

    cursor.execute(SQLQuery)

    items_data = cursor.fetchall()

    number_of_items = len(items_data)

    items = {}

    i = 0

    while i < number_of_items:
        items[str(i)] = {}
        items[str(i)]['item_id'] = items_data[i][0]
        items[str(i)]['item_name'] = items_data[i][1]
        items[str(i)]['item_cost'] = items_data[i][2]
        items[str(i)]['item_secret_shop'] = items_data[i][3]
        items[str(i)]['item_side_shop'] = items_data[i][4]
        items[str(i)]['item_recipe'] = items_data[i][5]
        i += 1

    return items

def get_win_rate(hero_id, matches_requested):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT count(*)
    FROM matches
    WHERE hero_id = :hero_id
    ORDER BY match_date_time DESC
    LIMIT {}
    
    '''

    cursor.execute(SQLQuery.format(matches_requested), {"hero_id": hero_id})
    recent_amount_of_games = cursor.fetchone()
    
    SQLQuery = '''
    
    SELECT count(*) 
    FROM matches 
    WHERE (hero_id = :hero_id AND ((radiant_win = 1 AND dire_team = 0) OR (radiant_win = 0 AND dire_team = 1))) 
    ORDER BY match_date_time DESC 
    LIMIT {}

    '''

    cursor.execute(SQLQuery.format(matches_requested), {"hero_id": hero_id})
    recent_amount_of_games_won = cursor.fetchone()

    win_rate_data = round((recent_amount_of_games_won[0] / recent_amount_of_games[0]) * 100, 2)

    return str(win_rate_data)