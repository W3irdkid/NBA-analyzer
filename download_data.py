from nba_api.stats.endpoints import leaguegamelog, leaguegamefinder, playergamestreakfinder, gamerotation, playercareerstats, PlayerGameLog
from nba_api.stats.static import players, teams

import pandas as pd

#Set default data
season = '2022-23' # Example season
player_id = '201939'  # Example player ID (Stephen Curry)
game_id = '0022200001'  # Example game ID
team_id = '1610612744'  # Example team ID (Golden State Warriors)

# Find team id by team name
def get_team_id_by_name(name):
    team = teams.find_teams_by_full_name(name)
    return team


# Get player info by ID
def get_player_career_info(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id).get_dict()
    columns = career['resultSets'][0]['headers']
    rows = career['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df

# Get  player id by name
def get_player_id_by_name(name):
    player = players.get_players()
    return player


# Get active random player ID
def get_random_player_id():
    randomPlayer = players.get_active_players()
    return randomPlayer.sample().values[0]['id']

# Get average stat by player_id
def get_avg_stat_by_id(player_id, stat): 
    career = PlayerGameLog(player_id=player_id).get_dict()
    columns = career['resultSets'][0]['headers']
    rows = career['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    result =  df[stat].mean()
    round_result = round(result,2)
    return round_result
 

# Get season data
def get_season_data(season):
    gamelog = leaguegamelog.LeagueGameLog(season=season).get_dict()
    columns = gamelog['resultSets'][0]['headers']
    rows = gamelog['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df

# Get data from many seasons (list needed for seasons)
def get_many_seasons_data(seasons):
    many_seasons_data = []
    for season in seasons:
        gamelog = leaguegamelog.LeagueGameLog(seasons=seasons).get_dict()
        columns = gamelog['resultSets'][0]['headers']
        rows = gamelog['resultSets'][0]['rowSet']
        df = pd.DataFrame(rows, columns=columns)
        many_seasons_data.append(df)
    final_df = pd.concat(many_seasons_data)
    return final_df


# Get GameID only from given season
def get_all_gameID(season):
    gamelog = leaguegamelog.LeagueGameLog(season=season).get_dict()
    columns = gamelog['resultSets'][0]['headers']
    rows = gamelog['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df['GAME_ID']


# Get game info
def get_game_info(game_id):
    game = leaguegamefinder.LeagueGameFinder(game_id_nullable=game_id).get_dict()
    columns = game['resultSets'][0]['headers']
    rows = game['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df


# Get Game Rotation
def get_game_rotation(gameId):
    rotations = gamerotation.GameRotation(game_id=gameId).get_dict()
    columns = rotations['resultSets'][0]['headers']
    rows = rotations['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df


# Get first and last gameID from given season
def get_max_and_min_gameId(season):
    gamelog = leaguegamelog.LeagueGameLog(season=season).get_dict()
    columns = gamelog['resultSets'][0]['headers']
    rows = gamelog['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df['GAME_ID'].max(), df['GAME_ID'].min()


# Return random gameID from given season
def get_random_gameId(season):
    gamelog = leaguegamelog.LeagueGameLog(season=season).get_dict()
    columns = gamelog['resultSets'][0]['headers']
    rows = gamelog['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df['GAME_ID'].sample().values[0]


# Return players which played in the game
def get_game_rotation(game_id): 
    rotations = gamerotation.GameRotation(game_id=game_id).get_dict()
    columns = rotations['resultSets'][0]['headers']
    rows = rotations['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df['PERSON_ID']

# Return stat for player, group by season
def get_playerInfo_regularSeason(player_id, seasonType='Regular Season'):
    player = playercareerstats.PlayerCareerStats(player_id=player_id).get_dict()
    columns = player['resultSets'][0]['headers']
    rows = player['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df

# Return games played for given player
def get_playergamelog(player_id, season, seasonType='Regular Season'):
    gameLog = PlayerGameLog(player_id=player_id, season=season).get_dict()
    columns = gameLog['resultSets'][0]['headers']
    rows = gameLog['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df


