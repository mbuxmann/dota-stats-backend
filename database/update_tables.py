from config import WebAPIKey, steam_id, requests, time
from get_match import get_match_details
from database import get_latest_match_id, get_latest_number_of_heroes_from_database, get_latest_number_of_items_from_database
from heroes import get_heroes
from get_items import get_items

debug = True

def update_heroes_table():

    url = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/"

    querystring = {

        'key': WebAPIKey

    }

    try:
        time.sleep(1)
        parsed_data = requests.request('GET', url, params=querystring,
                                       timeout=3).json()
    except TimeoutError:
        print('The request timed out')
    else:
        if debug:
            print('Request Received')

    # Get the latest number of heroes available from valve api
    number_of_heroes = 0
    for hero in parsed_data['result']['heroes']:
        number_of_heroes += 1

    # Get the number of heroes stored in the database
    number_of_heroes_from_database = get_latest_number_of_heroes_from_database()

    if number_of_heroes == number_of_heroes_from_database:
        return
    elif number_of_heroes != number_of_heroes_from_database:
        get_heroes()
    else:
        if debug:
            print('Error with updating heroes table')




def update_matches_tables():

    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/"

    querystring = {
        "matches_requested": 30,
        "account_id": steam_id,
        "key": WebAPIKey,
        "min_players": 10
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

    latest_match_id = parsed_data['result']['matches'][0]['match_id']

    latest_match_id_from_database = get_latest_match_id()

    if debug:
        print('latest_match_id:', latest_match_id)
        print('latest_match_id_from_database', latest_match_id_from_database)

    for match in parsed_data['result']['matches']:
        if match['match_id'] == latest_match_id_from_database:
            return
        elif match['match_id'] != latest_match_id_from_database:
            get_match_details(match['match_id'])
        else:
            if debug:
                print('Error with updating matches table')

def update_items_table():

    url = "https://api.steampowered.com/IEconDOTA2_570/GetGameItems/V001/"

    querystring = {

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

    # Get the latest number of items available from valve api
    number_of_items = 0
    for item in parsed_data['result']['items']:
        number_of_items += 1

    # Get the number of items stored in the database
    number_of_items_from_database = get_latest_number_of_items_from_database()

    if number_of_items == number_of_items_from_database:
        return
    elif number_of_items != number_of_items_from_database:
        get_items()
    else:
        if debug:
            print('Error with updating items table')

