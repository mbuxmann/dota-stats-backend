from config import matches_requested
from get_match import get_latest_matches
from heroes import get_heroes

def initialize():
    print('INITIALIZING')
    db.check_tables_exists()
    get_heroes()
    get_latest_matches(matches_requested)
    print('DONE INTIALIZING')

