from consume_api import get_all, insert_data
import json

file = open("leagues_json/premier_league.json", "r")
data = json.load(file)
file.close()

url = 'http://localhost:3000/leagues/'

insert_data(url, data)