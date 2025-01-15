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


def get_player_id_by_name(name):
    player = players.find_players_by_full_name(name)
    return player
#print(get_player_id_by_name('Stephen Curry'))


def get_avg_stat_by_id(player_id, stat):
    career = PlayerGameLog(player_id=player_id).get_dict()
    columns = career['resultSets'][0]['headers']
    rows = career['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    result =  df[stat].mean()
    round_result = round(result,2)
    return round_result

# avg_points = get_avg_stat_by_id(player_id, 'PTS')
# print(avg_points)


# Get season data
def get_season_data(season):
    gamelog = leaguegamelog.LeagueGameLog(season=season).get_dict()
    columns = gamelog['resultSets'][0]['headers']
    rows = gamelog['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df



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


#Get player game streaks
def player_streak(player_id):
    streaks = playergamestreakfinder.PlayerGameStreakFinder(player_id_nullable=player_id).get_dict()
    columns = streaks['resultSets'][0]['headers']
    rows = streaks['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df


# Get Game Rotation
def get_game_rotation(gameId):
    rotations = gamerotation.GameRotation(game_id=gameId).get_dict()
    columns = rotations['resultSets'][0]['headers']
    rows = rotations['resultSets'][0]['rowSet']
    df = pd.DataFrame(rows, columns=columns)
    return df



def player_streak_gt_pts(player_id, gt_pts):
    streaks = playergamestreakfinder.PlayerGameStreakFinder(
        player_id_nullable=player_id,
        gt_pts_nullable=gt_pts
    ).get_data_frames()[0]
    return streaks


# Przykład: LeBron James, punkty >20
# streaks_df = player_streak_gt_pts(player_id=2544, gt_pts=30)