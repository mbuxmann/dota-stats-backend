from config import requests, WebAPIKey, matches_requested, time
from database import check_hero_exists, add_hero

debug = True


def get_heroes():

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

    if debug:
        print('====== Heroes List ======')
    for hero in parsed_data['result']['heroes']:
        hero_id = hero['id']
        hero_name = hero['name'][14:]
        if not check_hero_exists(hero_id):
            add_hero(hero_id, hero_name)
