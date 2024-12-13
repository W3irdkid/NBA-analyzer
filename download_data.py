from nba_api.stats.endpoints import leaguegamelog
import pandas as pd

#Set season
season = '2022-23'

# Get season data
gamelog = leaguegamelog.LeagueGameLog(season=season).get_dict()

# Create DataFrame
df = pd.DataFrame(gamelog['resultSets'][0]['rowSet'])

# Save results
df.to_csv(f'wyniki_sezonu_{season}.csv', index=False)

print(f'Wyniki sezonu {season} zapisano do pliku')