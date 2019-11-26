import requests
import json
import time
import schedule
import sqlite3

debug = True
debug_heroes = False
#database = '/home/ubuntu/dota-stats-backend/database/database.db'
database = 'database.db'
matches_requested = 30
WebAPIKey = "7ED28ADAFD5EE5F46D041EF05E65E78F"
steam_id = 126747751

