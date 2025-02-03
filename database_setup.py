import sqlite3
import download_data as dd

def create_database_structure():
    try:
        with sqlite3.connect('nba_stats.db') as conn:
            cursor = conn.cursor()
            
            # Create players average stats table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS playersAvgStats (
                    player_id INTEGER PRIMARY KEY,
                    avg_min REAL NOT NULL,
                    avg_fgm REAL NOT NULL,
                    avg_fga REAL NOT NULL,
                    avg_fg_pct REAL NOT NULL,
                    avg_fg3m REAL NOT NULL,
                    avg_fg3a REAL NOT NULL,
                    avg_fg3_pct REAL NOT NULL,
                    avg_ftm REAL NOT NULL,
                    avg_fta REAL NOT NULL,
                    avg_ft_pct REAL NOT NULL,
                    avg_oreb REAL NOT NULL,
                    avg_dreb REAL NOT NULL,
                    avg_reb REAL NOT NULL,
                    avg_ast REAL NOT NULL,
                    avg_stl REAL NOT NULL,
                    avg_blk REAL NOT NULL,
                    avg_tov REAL NOT NULL,
                    avg_pf REAL NOT NULL,
                    avg_pts REAL NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS AvgTeamStats (
                    team_id INTEGER PRIMARY KEY,
                    avg_pts REAL NOT NULL,
                    win_pct REAL NOT NULL,
                    avg_fgm REAL NOT NULL,
                    avg_fga REAL NOT NULL,
                    avg_fg_pct REAL NOT NULL,
                    avg_fg3m REAL NOT NULL,
                    avg_fg3a REAL NOT NULL,
                    avg_fg3_pct REAL NOT NULL,
                    avg_ftm REAL NOT NULL,
                    avg_fta REAL NOT NULL,
                    avg_ft_pct REAL NOT NULL,
                    avg_oreb REAL NOT NULL,
                    avg_dreb REAL NOT NULL,
                    avg_reb REAL NOT NULL,
                    avg_ast REAL NOT NULL,
                    avg_stl REAL NOT NULL,
                    avg_blk REAL NOT NULL,
                    avg_tov REAL NOT NULL,
                    avg_pf REAL NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS TeamWinStreaks (
                    team_id INTEGER,
                    season TEXT,
                    win_streak INTEGER,
                    longest_win_streak INTEGER,
                    avg_win_streak_length REAL,
                    home_win_streak_pct REAL,
                    away_win_streak_pct REAL,
                    FOREIGN KEY(team_id) REFERENCES AvgTeamStats(team_id)
                    )
''')
            # Connection and transaction auto-commit handled by context manager
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise

if __name__ == '__main__':
    create_database_structure()