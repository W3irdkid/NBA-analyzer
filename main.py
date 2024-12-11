from nba_api.live.nba.endpoints import scoreboard

# Get today's gamesgit 
scores = scoreboard.ScoreBoard()
def get_gameId():
    games = scores.games.get_dict()  # Pobieramy słownik gier
    for game in games:
        game_id = game['gameId']
        home_team = game['homeTeam']['teamName']  # Poprawiony dostęp do teamName
        away_team = game['awayTeam']['teamName']  # Poprawiony dostęp do teamName
        
        print(f'Game ID: {game_id}')
        print(f'Home Team: {home_team}')
        print(f'Away Team: {away_team}')

user_input = input("Do u want to check today games? (Y/N): ")
if user_input == "Y":
    get_gameId()
elif user_input == "N": 
    print("Bye!")
    exit()
else:
    exit()

