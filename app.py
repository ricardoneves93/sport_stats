import requests
import pymongo
import json
import queries

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['football_stats']

leagues = {("PT_1", "457"), ("EN_1", "445"), ("SP_1", "455"), 
("FR_1", "450"), ("IT_1", "456")}

main_url = "http://api.football-data.org/v1/competitions/"
fixtures_url = "/fixtures"

url_portuguese = "http://api.football-data.org/v1/competitions/457/fixtures"
url_english = "http://api.football-data.org/v1/competitions/445/fixtures"
url_spanish = "http://api.football-data.org/v1/competitions/455/fixtures"
url_french = "http://api.football-data.org/v1/competitions/451/fixtures"
url_italian = "http://api.football-data.org/v1/competitions/456/fixtures"
headers = {'X-Auth-Token': 'c79a7e5516fc4e76807286312ff87595'}


def get_league_fixtures(league_id):
	print("Getting league: " + league_id)
	url = main_url + league_id + fixtures_url
	r = requests.get(url, headers)
	json_obj = json.loads(r.content)
	fixtures_array = json_obj['fixtures']
	for fixture in fixtures_array:
		if fixture['status'] == 'FINISHED':
			new_fixture = {}
			new_fixture["league"] = league_id
			new_fixture["date"] = fixture["date"]
			new_fixture["status"] = fixture["status"]
			new_fixture["matchday"] = fixture["matchday"]
			new_fixture["homeTeam"] = fixture["homeTeamName"]
			new_fixture["awayTeam"] = fixture["awayTeamName"]
			new_fixture["result"] = fixture["result"]
			db.football_stats.insert_one(new_fixture).inserted_id

def empty_database():
	print("Deleting database...")
	db.football_stats.delete_many({})

# Delete all old data
empty_database()

# Get new data
for league_name, league_id in leagues:
	get_league_fixtures(league_id)



