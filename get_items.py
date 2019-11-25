from config import WebAPIKey, requests, json, time
from database import check_item_exists, add_item
debug = False

def get_items():

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

    if debug:
        print('====== Item List ======')
    
    for item in parsed_data['result']['items']:
        item_id = item['id']
        item_name = item['name'][5:]
        item_cost = item['cost']
        item_secret_shop = item['secret_shop']
        item_side_shop = item['side_shop']
        item_recipe = item['recipe']

        if not check_item_exists(item_id):
            add_item(item_id, item_name, item_cost, item_secret_shop, 
                item_side_shop, item_recipe)