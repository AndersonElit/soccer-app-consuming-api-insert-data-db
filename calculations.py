
class calculations():

    def results(self, matches):

        all_matches = []

        for item in matches:

            match_set = []

            for match in item:

                date = int(match[0])
                local = match[1]
                visit = match[2]
                goals_local = int(match[3])
                goals_visit = int(match[4])
                result = ''

                if goals_local > goals_visit:
                    result = 'VL'
                elif goals_local < goals_visit:
                    result = 'VV'
                elif goals_local == goals_visit:
                    result = 'E'

                newdata = [date, local, visit, goals_local, goals_visit, result]
                match_set.append(newdata)

            all_matches.append(match_set)
        
        return all_matches

    '''
    def CS(self, teams, matches):

        for team in teams:

    '''
