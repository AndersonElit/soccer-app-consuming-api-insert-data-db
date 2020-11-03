import requests
import json

# get all data
def get_all(url):
    res = requests.get(url)
    json_data = res.json()
    return json_data

# insert a new item
def insert_data(url, data):
    res = requests.post(url, json=data)
    json_data = res.json()
    print(f"data for {json_data['league']} team were inserted in DB")
    return ''