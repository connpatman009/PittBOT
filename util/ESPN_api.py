import requests

MENS_BASKETBALL_URL = "http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/pittsburgh"

def get_next_game_basketball() -> dict:
	ESPN_data = requests.get(MENS_BASKETBALL_URL).json()
	next_game = None
	opponent_name = None
	try:
		next_game = ESPN_data["team"]["nextEvent"][0]["competitions"][0]
		date_and_time = next_game["date"]
		location = next_game["venue"]
		if next_game["competitors"][0]["id"] == "221":		# Pitt's Men's Basketball team id is 221
			opponent_name = next_game["competitors"][1]["team"]["displayName"]
		elif next_game["competitors"][1]["id"] == "221":
			opponent_name = next_game["competitors"][0]["team"]["displayName"]
		else:
			opponent_name = "Couldn't find opponent"
		return {
			"date_and_time": date_and_time,
			"location": location,
			"opponent_name": opponent_name,
			"valid": "true"
		}
	except IndexError:
		return {"valid": "false"}
