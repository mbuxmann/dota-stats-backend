from config import matches_requested, time, schedule
from get_match import get_latest_matches
from heroes import get_heroes
from get_items import get_items
from update_tables import update_heroes_table, update_items_table, update_matches_tables
import database as db
import update_tables


from config import database

def initialize():
    print('INITIALIZING')
    db.check_tables_exists()
    get_heroes()
    get_latest_matches(30)
    print('DONE INTIALIZING')

def update():
    print('UPDATING TABLES')
    update_heroes_table()
    update_matches_tables()
    update_items_table()
    print('DONE UPDATING TABLES')
    
initialize()
schedule.every().hour.do(update)


while True:
    schedule.run_pending()
    time.sleep(1)