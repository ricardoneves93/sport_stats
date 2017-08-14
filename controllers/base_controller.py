from flask import Flask
from flask import jsonify
from flask import request
from services import stats_service
app = Flask(__name__)

@app.route('/stats', methods=['GET'])
def hello_world():
	team_name = request.headers.get('team-name')
	if team_name is not None:
		return stats_service.get_team_stats(team_name)
	else:
		return "Error, please provide a team"
		