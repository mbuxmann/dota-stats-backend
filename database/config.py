import requests
import json
import time
import schedule
import pg8000

debug = False
debug_heroes = False
database = 'database.db'
matches_requested = 3
WebAPIKey = "7ED28ADAFD5EE5F46D041EF05E65E78F"
steam_id = 126747751
user = "vgajljwoqlrgmi"
password = "095b820e91cec4915c71d18a237aa898a180b6cd7a8e189bd3c7364c6eacb862"
host = "ec2-54-246-98-119.eu-west-1.compute.amazonaws.com"
port = 5432
database = "dffon80rotpm9n"
