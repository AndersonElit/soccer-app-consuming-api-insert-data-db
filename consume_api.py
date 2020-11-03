import requests
import json

# get all data
def get_league(url, league):
    res = requests.post(url, json=league)
    json_data = res.json()
    return json_data

# insert a new item
def insert_league(url, data):
    res = requests.post(url, json=data)
    json_data = res.json()
    print(f"data for temp {json_data['temp']} were inserted in DB")
    return ''