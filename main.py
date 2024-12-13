from nba_api.live.nba.endpoints import scoreboard


# Get today's gamesgit 
scores = scoreboard.ScoreBoard()

def get_game_id():
    games = scores.games.get_dict()
    for game in games:
        game_id = game['gameId']
        home_team = game['homeTeam']['teamName']
        away_team = game['awayTeam']['teamName']
        
        print(f'Game ID: {game_id}')
        print(f'Home Team: {home_team}')
        print(f'Away Team: {away_team}')


user_input = input("Do u want to check today games? (y/n): ").strip().lower()
if user_input == "y":
    get_game_id()
elif user_input == "n":
    print("Bye!")
    exit()
else:
    exit()
