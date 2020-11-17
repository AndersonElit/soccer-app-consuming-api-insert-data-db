from get_data import get_data
from calculations import calculations

gd = get_data()
cl = calculations()

y1 = 1992
y2 = 1993

while y1 <= 2018 and y2 <= 2019:

    # get teams list
    teams = gd.get_teams(y1, y2)

    # get matches
    matches = gd.get_matches(y1, y2)

    # add results to each match
    matches_results = cl.results(matches)