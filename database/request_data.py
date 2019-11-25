 import sqlite3
from config import database, debug
import ast

debug = True


# Gets the match ids from latest requested matches
def get_recent_matches(matches_requested):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT match_id
    FROM 'matches'
    ORDER BY match_date_time DESC
    LIMIT {}

    '''

    cursor.execute(SQLQuery.format(matches_requested))

    match_ids = cursor.fetchall()

    cursor.close()
    connection.close()

    for match_id in match_ids:
        get_match_result(match_id[0])


# Gets the match ids from the latest request matches by hero id
def get_recent_matches_by_hero(hero_id, matches_requested):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT match_id
    FROM 'matches'
    WHERE hero_id = {}
    ORDER BY match_date_time DESC
    LIMIT {}

    '''

    cursor.execute(SQLQuery.format(hero_id, matches_requested))

    match_ids = cursor.fetchall()

    cursor.close()
    connection.close()
    for match_id in match_ids:
        get_match_result(match_id[0])


def get_match_result(match_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT *
    FROM 'matches'
    WHERE match_id = :match_id

    '''

    cursor.execute(SQLQuery, {'match_id': match_id})

    match_data = cursor.fetchone()

    cursor.close()
    connection.close()

    match_number = match_data[0]
    match_id = match_data[1]
    game_mode = match_data[2]
    radiant_win = match_data[3]
    hero_id = match_data[4]
    hero_level = match_data[5]
    kills = match_data[6]
    deaths = match_data[7]
    assists = match_data[8]
    last_hits = match_data[9]
    denies = match_data[10]
    gold_per_min = match_data[11]
    xp_per_min = match_data[12]
    hero_damage = match_data[13]
    tower_damage = match_data[14]
    hero_healing = match_data[15]
    remaining_gold = match_data[16]
    gold_spent = match_data[17]
    item_list = ast.literal_eval(match_data[18])
    backpack_list = ast.literal_eval(match_data[19])
    hero_abilities = ast.literal_eval(match_data[20])
    first_blood_time = match_data[21]
    match_duration = match_data[22]
    match_seq_num = match_data[23]
    leaver_status = match_data[24]
    match_date_time = match_data[25]
    inserted_date_time = match_data[26]

    if debug:
        print('====== MATCH: ' + str(match_id) + " RESULTS ======")
        print('Match number:', match_number)
        print('Match id:', match_id)
        print('Game mode:', game_mode)
        print('Radiant win', radiant_win)
        print('Hero id:', hero_id)
        print('Hero level:', hero_level)
        print('Kills:', kills)
        print('Deaths:', deaths)
        print('Assists:', assists)
        print('Last hits:', last_hits)
        print('Denies:', denies)
        print('Gold per min:', gold_per_min)
        print('Xp per min:', xp_per_min)
        print('Hero damage:', hero_damage)
        print('Tower damage:', tower_damage)
        print('Hero healing:', hero_healing)
        print('Remaining gold:', remaining_gold)
        print('Gold spent:', gold_spent)
        print('Item list:', item_list)
        print('Backpack list:', backpack_list)
        print('Hero abilities:', hero_abilities)
        print('First blood time:', first_blood_time)
        print('Match duration:', match_duration)
        print('Match seq num:', match_seq_num)
        print('Leaver status:', leaver_status)
        print('Match date time:', match_date_time)
        print('Inserted date time:', inserted_date_time)


# TODO: change radiant_win to keep track of won or not
def get_averages_of_latest_matches(matches_requested):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT
    radiant_win, avg(kills), avg(deaths), avg(assists), avg(last_hits), avg(denies), avg(gold_per_min),
    avg(xp_per_min), avg(hero_damage), avg(tower_damage), avg(hero_healing), avg(remaining_gold) +
    avg(gold_spent)
    FROM 'matches'
    ORDER BY match_date_time DESC
    LIMIT {}
    '''

    cursor.execute(SQLQuery.format(matches_requested))

    data = cursor.fetchone()

    if debug:
        print('Average Kills:', round(data[1]))
        print('Average Deaths:', round(data[2]))
        print('Average Assists:', round(data[3]))
        print('Average Last Hits:', round(data[4]))
        print('Average Denies:', round(data[5]))
        print('Average GPM:', round(data[6]))
        print('Average XPM:', round(data[7]))
        print('Average Hero Damage:', round(data[8]))
        print('Average Tower Damage:', round(data[9]))
        print('Average Hero Healing:', round(data[10]))
        print('Average Net Worth:', round(data[11]))

    cursor.close()
    connection.close()


def get_averages_of_latest_matches_by_hero(matches_requested, hero_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    SQLQuery = '''

    SELECT
    radiant_win, avg(kills), avg(deaths), avg(assists), avg(last_hits), avg(denies), avg(gold_per_min),
    avg(xp_per_min), avg(hero_damage), avg(tower_damage), avg(hero_healing), avg(remaining_gold) +
    avg(gold_spent)
    FROM 'matches'
    WHERE hero_id = :hero_id
    ORDER BY match_date_time DESC
    LIMIT {}
    '''

    cursor.execute(SQLQuery.format(matches_requested), {'hero_id': hero_id})

    data = cursor.fetchone()

    if debug:
        print('Hero ID:', hero_id)
        print('Average Kills:', round(data[1]))
        print('Average Deaths:', round(data[2]))
        print('Average Assists:', round(data[3]))
        print('Average Last Hits:', round(data[4]))
        print('Average Denies:', round(data[5]))
        print('Average GPM:', round(data[6]))
        print('Average XPM:', round(data[7]))
        print('Average Hero Damage:', round(data[8]))
        print('Average Tower Damage:', round(data[9]))
        print('Average Hero Healing:', round(data[10]))
        print('Average Net Worth:', round(data[11]))

    cursor.close()
    connection.close()
