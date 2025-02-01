import sqlite3


conn = sqlite3.connect('nba_stats.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
               game_id TEXT PRIMARY KEY,
               home_team TEXT,
               away_team TEXT,
               date TEXT
               )
''')




conn.commit()
conn.close()