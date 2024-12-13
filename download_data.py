from nba_api.stats.endpoints import leaguegamelog
import pandas as pd

#Set season
season = '2022-23'

# Get season data
gamelog = leaguegamelog.LeagueGameLog(season=season).get_dict()
columns = gamelog['resultSets'][0]['headers']
rows = gamelog['resultSets'][0]['rowSet']


# Create DataFrame
df = pd.DataFrame(rows, columns=columns)

# Save results
#df.to_csv(f'wyniki_sezonu_{season}.csv', index=False)

#print(f'Wyniki sezonu {season} zapisano do pliku')
print(df.head())
print(df.describe())
print(df['TEAM_ID'].unique())
