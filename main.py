from nba_api.live.nba.endpoints import scoreboard
import sqlite3
import pandas as pd


def import_csv_as_table(csv_file, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists='replace', index = False)
    conn.commit()
    conn.close()


#import_csv_as_table('Season_2022-23.csv.csv', 'nba_stats.db', 'Season_2022-23')
