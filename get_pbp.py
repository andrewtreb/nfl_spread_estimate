import requests
import os



class DataRetrival:
    def __init__(self):
        self.espn_base_url = "http://site.api.espn.com"

    def refresh_nfl_teams(self):
        url  = self.espn_base_url + "/apis/site/v2/sports/football/nfl/teams"

        ret = requests.get(url)

        f = open('data/teams.json',"w")
        f.write(ret.text)

        f.close()
        self.team_json = 'data/teams.json'

    def get_nfl_league_id(self):
        
        


base = DataRetrival()
base.refresh_nfl_teams()