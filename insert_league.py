from consume_api import get_all, insert_data
import json

file = open("leagues_json/premier_league.json", "r")
data = json.load(file)
file.close()

url = 'http://localhost:3000/leagues/'

league_name = data['league']
temps = data['temps']

for item in temps:

    temp = item['temp']
    teams = item['teams']
    dates = item['dates']

    temp_obj = {
        "league": league_name,
        "temp": temp,
        "teams": teams,
        "dates": dates
    }

    insert_data(url, temp_obj)

