from nba_api.live.nba.endpoints import scoreboard
import sqlite3
import pandas as pd
import download_data as dd


#conn = sqlite3.connect('nba_stats.db')
#c = conn.cursor()


def import_csv_as_table(csv_file, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists='replace', index = False)
    conn.commit()
    conn.close()


def import_df_to_sqlite(df, db_name, table_name, if_exists='fail', index=False):
    with sqlite3.connect(db_name) as conn:
        df.to_sql(table_name, conn, if_exists=if_exists, index=index)
    df = dd.get_playergamelog(player_id=201939, season="2023-24", seasonType="Regular Season")



'''
Just tried to get random set of players from random game (both teams)

randomPlayerId = dd.get_random_player_id()
randomId = dd.get_random_gameId("2022-23")
rotation = dd.get_game_rotation(randomId)
rotation.to_excel('rotation.xlsx')
print('Rotation saved to rotation.xlsx')

many_player_log = dd.get_playergamelog(randomPlayerId, "2023-24")
many_player_log.to_excel('many_player_log.xlsx')
print('Many player log saved to many_player_log.xlsx')'''





