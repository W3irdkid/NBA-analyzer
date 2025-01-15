from nba_api.live.nba.endpoints import scoreboard
import sqlite3


conn = sqlite3.connect('nba_stats.db')
cursor = conn.cursor()


# Get today's gamesgit 
scores = scoreboard.ScoreBoard()

def get_game_id():
    games = scores.games.get_dict()
    for game in games:
        game_id = game['gameId']
        home_team = game['homeTeam']['teamName']
        away_team = game['awayTeam']['teamName']
        game_date = game['gameTimeUTC']
        
        print(f'Game ID: {game_id}')
        print(f'Home Team: {home_team}')
        print(f'Away Team: {away_team}')

cursor.execute('''
    INSERT OR IGNORE INTTO games (game_id, home_team, away_team, date)
    VALUES (?, ?, ?, ?)
''', (game_id, home_team, away_team, game_date))
print(f'Game ID: {game_id}, Home Team: {home_team}, Away Team: {away_team}, Date: {game_date}')

user_input = input("Do u want to check today games? (y/n): ").strip().lower()
if user_input == "y":
    get_game_id()
elif user_input == "n":
    print("Bye!")
    exit()
else:
    exit()
