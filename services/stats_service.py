from flask import jsonify
from repositories import queries

def get_team_stats(team_name):
	number_victories = queries.get_team_number_victories(team_name)
	number_draws = queries.get_team_number_draws(team_name)
	number_defeats = queries.get_team_number_defeats(team_name)
	number_recevied_goals = queries.get_team_received_goals(team_name)
	number_scored_goals = queries.get_team_scored_goals(team_name)
	number_played_matches = queries.get_matches_played_by_team(team_name)
	return jsonify(
		victories=number_victories,
		draws=number_draws, 
		defeats=number_defeats,
		received_goals=number_recevied_goals,
		scored_goals=number_scored_goals,
		matches_played=number_played_matches
		)
