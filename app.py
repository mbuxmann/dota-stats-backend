from flask import Flask, request
from flask_cors import CORS, cross_origin

database = 'database.db'

app = Flask(__name__)
cors = CORS(app)

@app.route('/GetHeroes/')
@cross_origin()
def get_heroes():
    from functions import get_heroes
    heroes = get_heroes()
    return heroes


@app.route('/GetRecentMatches/')
def get_recent_matches():
    from functions import get_recent_matches
    matches_requested = request.args.get('matches_requested')
    hero_id = request.args.get('hero_id')
    matches = get_recent_matches(matches_requested, hero_id)
    return matches


@app.route('/GetAveragesOfLatestMatches/')
def get_averages_of_latest_matches():
    from functions import get_averages_of_latest_matches
    matches_requested = request.args.get('matches_requested')
    hero_id = request.args.get('hero_id')
    data = get_averages_of_latest_matches(matches_requested, hero_id)
    return data

@app.route('/GetItems/')
def get_items():
    from functions import get_items
    items = get_items()
    return items

@app.route('/GetWinRate/')
def get_win_rate():
    from functions import get_win_rate
    matches_requested = request.args.get('matches_requested')
    hero_id = request.args.get('hero_id')
    win_rate_data = get_win_rate(hero_id, matches_requested)
    return win_rate_data

if __name__ == '__main__':
    app.run()
