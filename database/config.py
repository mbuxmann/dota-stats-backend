import requests
import json
import time
import sqlite3

debug = True
debug_heroes = False
database = '/home/ubuntu/dota-stats-backend/database/database.db'
#database = 'database.db'
matches_requested = 30
WebAPIKey = WEBAPIKEY
steam_id = 126747751

