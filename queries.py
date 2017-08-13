from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['football_stats']

# Queries

# Get results by team
def get_results_by_team(team_name):
	search_dict = {'$or': [{'homeTeam': team_name}, {'awayTeam': team_name}]}
	return db.football_stats.find(search_dict)

def get_team_scored_goals(team_name):
	scored_goals = 0
	search_home_team = {'homeTeam': team_name}
	search_away_team = {'awayTeam': team_name}
	
	results = db.football_stats.find(search_home_team)
	for result in results:
		scored_goals += result["result"]["goalsHomeTeam"]

	results = db.football_stats.find(search_away_team)
	for result in results:
		scored_goals += result["result"]["goalsAwayTeam"]
	return scored_goals

def get_team_received_goals(team_name):
	received_goals = 0
	search_home_team = {'homeTeam': team_name}
	search_away_team = {'awayTeam': team_name}
	
	results = db.football_stats.find(search_home_team)
	for result in results:
		received_goals += result["result"]["goalsAwayTeam"]

	results = db.football_stats.find(search_away_team)
	for result in results:
		received_goals += result["result"]["goalsHomeTeam"]
	return received_goals

def get_team_number_victories(team_name):
	number_victories = 0
	search_home_team = {'homeTeam': team_name}
	search_away_team = {'awayTeam': team_name}
	
	results = db.football_stats.find(search_home_team)
	for result in results:
		received_goals = result["result"]["goalsAwayTeam"]
		scored_goals = result["result"]["goalsHomeTeam"]
		if scored_goals > received_goals:
			number_victories += 1

	results = db.football_stats.find(search_away_team)
	for result in results:
		received_goals += result["result"]["goalsHomeTeam"]
		scored_goals = result["result"]["goalsAwayTeam"]
		if scored_goals > received_goals:
			number_victories += 1
	return number_victories

def get_team_number_defeats(team_name):
	number_defeats = 0
	search_home_team = {'homeTeam': team_name}
	search_away_team = {'awayTeam': team_name}
	
	results = db.football_stats.find(search_home_team)
	for result in results:
		received_goals = result["result"]["goalsAwayTeam"]
		scored_goals = result["result"]["goalsHomeTeam"]
		if scored_goals < received_goals:
			number_defeats += 1

	results = db.football_stats.find(search_away_team)
	for result in results:
		received_goals += result["result"]["goalsHomeTeam"]
		scored_goals = result["result"]["goalsAwayTeam"]
		if scored_goals < received_goals:
			number_defeats += 1
	return number_defeats

def get_team_number_draws(team_name):
	number_draws = 0
	search_home_team = {'homeTeam': team_name}
	search_away_team = {'awayTeam': team_name}
	
	results = db.football_stats.find(search_home_team)
	for result in results:
		received_goals = result["result"]["goalsAwayTeam"]
		scored_goals = result["result"]["goalsHomeTeam"]
		if scored_goals == received_goals:
			number_draws += 1

	results = db.football_stats.find(search_away_team)
	for result in results:
		received_goals += result["result"]["goalsHomeTeam"]
		scored_goals = result["result"]["goalsAwayTeam"]
		if scored_goals == received_goals:
			number_draws += 1
	return number_draws