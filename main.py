from config import matches_requested
from get_match import get_latest_matches
from heroes import get_heroes
from get_items import get_items
from update_tables import update_heroes_table, update_items_table, update_matches_tables
import database as db
import update_tables
import sqlite3

from config import database

def initialize():
    print('INITIALIZING')
    db.check_tables_exists()
    get_heroes()
    get_latest_matches(30)

def update():
    print('UPDATING TABLES')
    update_heroes_table()
    update_matches_tables()
    update_items_table()
