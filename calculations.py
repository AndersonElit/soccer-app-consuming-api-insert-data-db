
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

    def data_calculations(self, teams, matches):

        for team in teams:

            cs_l, cs_v, fts_l, fts_v = 0, 0, 0, 0
            p_15_l, l_15_l, p_25_l, l_25_l, bts_l = 0, 0, 0, 0, 0
            p_15_v, l_15_v, p_25_v, l_25_v, bts_v = 0, 0, 0, 0, 0
            pw_l, pw_v, pe_l, pe_v, pl_l, pl_v = 0, 0, 0, 0, 0, 0
            numd_l, numd_v = 0, 0
            local_matches = []
            visit_matches = []

            for date in matches:
                for match in date:

                    ndate = int(match[0])
                    local = match[1]
                    visit = match[2]
                    goals_l = int(match[3])
                    goals_v = int(match[4])
                    goals_t = goals_l + goals_v

                    if team == local:

                        numd_l += 1

                        if goals_l == 0:
                            fts_l += 1
                        elif goals_v == 0:
                            cs_l += 1
                        elif goals_l > goals_v:
                            pw_l += 1
                        elif goals_l < goals_v:
                            pl_l += 1
                        elif goals_l == goals_v:
                            pe_l += 1

                        if goals_t > 1:
                            p_15_l += 1
                        elif goals_t < 1:
                            l_15_l += 1
                        elif goals_t > 2:
                            p_25_l += 1
                        elif goals_t < 2:
                            l_25_l += 1
                        
                        if goals_l > 0 and goals_v > 0:
                            bts_l += 1

                    if team == visit:

                        numd_v += 1

                        if goals_l == 0:
                            cs_v += 1
                        elif goals_v == 0:
                            fts_v += 1
                        elif goals_l > goals_v:
                            pl_v += 1
                        elif goals_l < goals_v:
                            pw_v += 1
                        elif goals_l == goals_v:
                            pe_v += 1

                        if goals_t > 1:
                            p_15_v += 1
                        elif goals_t < 1:
                            l_15_v += 1
                        elif goals_t > 2:
                            p_25_v += 1
                        elif goals_t < 2:
                            l_25_v += 1

                        if goals_l > 0 and goals_v > 0:
                            bts_v += 1

        return 0
        

    
