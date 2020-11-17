import pickle
import json

class get_data():

    # get teams list
    def get_teams(self, y1, y2):
        file_teams_path = f"../BOT-matches-retriever/premier_league/teams/teams_{str(y1)}_{str(y2)}"
        binary_file_teams = open(file_teams_path, "rb")
        teams = pickle.load(binary_file_teams)
        binary_file_teams.close()
        return teams

    def get_matches(self, y1, y2):
        file_matches_path = f"../BOT-matches-retriever/premier_league/matches/matches_{str(y1)}_{str(y2)}"
        binary_file_matches = open(file_matches_path, "rb")
        matches = pickle.load(binary_file_matches)
        binary_file_matches.close()
        return matches             