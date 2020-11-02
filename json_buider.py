import pickle
import json
from bash import bash

y1 = 1992
y2 = 1993

temps_list = []

while y1 <= 2018 and y2 <= 2019:

    # get teams list
    file_teams_path = f"../BOT-matches-retriever/premier_league/teams/teams_{str(y1)}_{str(y2)}"
    binary_file_teams = open(file_teams_path, "rb")
    teams = pickle.load(binary_file_teams)
    binary_file_teams.close()

    # get matches list
    file_matches_path = f"../BOT-matches-retriever/premier_league/matches/matches_{str(y1)}_{str(y2)}"
    binary_file_matches = open(file_matches_path, "rb")
    matches = pickle.load(binary_file_matches)
    binary_file_matches.close()

    # create dictionary with matches per date
    i = 0
    dates_list = []

    for item in matches:
        matches_list = []
        for match in item:
            match_obj = {
                "local": match[1],
                "visit": match[2],
                "goals_local": int(match[3]),
                "goals_visit": int(match[4])
            }
            matches_list.append(match_obj)
        matches_obj = {
            "date": i + 1,
            "matches": matches_list
        }
        dates_list.append(matches_obj)
        i += 1
    
    temp_obj = {
        "temp": f"{str(y1)}-{str(y2)}",
        "teams": teams,
        "dates": dates_list
    }

    temps_list.append(temp_obj)    

    y1 += 1
    y2 += 1

league_obj = {
    "league": "premier league",
    "temps": temps_list
}

json_file = open("premier_league.json", "w")
json.dump(league_obj, json_file, indent = 3)
json_file.close()
bash('mv premier_league.json leagues_json')