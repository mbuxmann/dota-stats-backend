from config import WebAPIKey, steam_id, requests, json, time
from database import check_match_exists, add_match

debug = False


# Gets the latest 30 public matches
def get_latest_matches(matches_requested=30, hero_id=None,
                       account_id=steam_id):

    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/"

    querystring = {
        "matches_requested": matches_requested,
        "account_id": steam_id,
        "key": WebAPIKey,
        "hero_id": hero_id,
        "min_players": 10,
        # "start_at_match_id": string(5085026589)
    }

    try:
        time.sleep(1)
        parsed_data = requests.request("GET", url, params=querystring,
                                       timeout=3).json()
    except TimeoutError:
        print('The request timed out')
    else:
        if debug:
            print('Request Received')

    # return match ID's
    for match in parsed_data['result']['matches']:
        get_match_details(str(match['match_id']))


# Retrieves stats from public games
def get_match_details(match_id):

    url = "http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/"

    querystring = {
        "match_id": match_id,
        "key": WebAPIKey
    }

    try:
        time.sleep(1)
        parsed_data = requests.request("GET", url, params=querystring,
                                       timeout=3).json()
    except TimeoutError:
        print('The request timed out')
    else:
        if debug:
            print('Request Received')

    # Check if data has expired yet from valve
    if 'hero_damage' not in parsed_data['result']['players'][0]:
        if debug:
            print('Match Data Expired')
        return

    radiant_win = int(parsed_data['result']['radiant_win'])
    match_date_time = parsed_data['result']['start_time']
    match_duration = parsed_data['result']['duration']
    match_seq_num = parsed_data['result']['match_seq_num']
    first_blood_time = parsed_data['result']['first_blood_time']
    game_mode = parsed_data['result']['game_mode']
    match_id = match_id

    if debug:
        print("====== Match Number: " + str(match_id) + " ======")
        print('radiant win:', radiant_win)
        print('date and time of match:', match_date_time)
        print('match_duration:', match_duration)
        print('match_seq_num:', match_seq_num)
        print('first_blood:', first_blood_time)
        print('game_mode:', game_mode)
        print('match id:', match_id)

    for player in parsed_data['result']['players']:
        if player['account_id'] == steam_id:
            hero_id = player['hero_id']
            kills = player['kills']
            deaths = player['deaths']
            assists = player['assists']
            leaver_status = player['leaver_status']
            last_hits = player['last_hits']
            denies = player['denies']
            gold_per_min = player['gold_per_min']
            xp_per_min = player['xp_per_min']
            hero_level = player['level']
            hero_damage = player['hero_damage']
            tower_damage = player['tower_damage']
            hero_healing = player['hero_healing']
            remaining_gold = player['gold']
            gold_spent = player['gold_spent']
            dire_team = bin(player['player_slot'])[2:].zfill(8)[0]

            item_list = []
            item_list.append(player['item_0'])
            item_list.append(player['item_1'])
            item_list.append(player['item_2'])
            item_list.append(player['item_3'])
            item_list.append(player['item_4'])
            item_list.append(player['item_5'])

            backpack_list = []
            backpack_list.append(player['backpack_0'])
            backpack_list.append(player['backpack_1'])
            backpack_list.append(player['backpack_2'])

            # convert list to string to store in database
            items_json = json.dumps(item_list)
            backpack_json = json.dumps(backpack_list)
            hero_abilities = json.dumps(player['ability_upgrades'])

            # check if match exists otherwise INSERT data
            if not check_match_exists(match_id):
                add_match(match_id, game_mode, radiant_win, dire_team,
                          hero_id, hero_level, kills, deaths, assists,
                          last_hits, denies, gold_per_min, xp_per_min,
                          hero_damage, tower_damage, hero_healing,
                          remaining_gold, gold_spent, items_json,
                          backpack_json, hero_abilities, first_blood_time,
                          match_duration, match_seq_num, leaver_status,
                          match_date_time)

            # Output
            if debug:
                print('Match ID', match_id)
                print('Hero ID:', hero_id)
                print('Kills:', kills)
                print('Deaths:', deaths)
                print('Assists:', assists)
                print('Leaver Status:', leaver_status)
                print('last_hits:', last_hits)
                print('Denies:', denies)
                print('Gold Per Minute:', gold_per_min)
                print('XP Per Minute:', xp_per_min)
                print('Hero Level:', hero_level)
                print('Hero Damage:', hero_damage)
                print('Tower Damage:', tower_damage)
                print('Hero Healing:', hero_healing)
                print('Remaining gold:', remaining_gold)
                print('Gold Spent:', gold_spent)
                print('Item List:', item_list)
                print('Backpack List:', backpack_list)
                print('Radiant Team:', dire_team)

#  LocalWords:  steampowered
