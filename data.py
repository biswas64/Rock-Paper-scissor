import sqlite3
import pandas as pd
def create_connection():
    try:
        
        return sqlite3.connect("rcp.db")

    except Exception as e:
        print(f"Error: {e}")

def create_table():
    connection  =  create_connection()
    try:
        with connection:
            create =  """
                CREATE TABLE IF NOT EXISTS data(
                playerId  INTEGER primary key,
                Name TEXT,
                GamesPlayed INTEGER ,
                Wins INTEGER ,
                Loss INTEGER ,
                Draw INTEGER 
                );

            """
            connection.execute(create)
     
    except Exception as e:
        print(f"Error: {e}")
def add_data(Name,GamesPlayed, Wins,Loss,Draw):
    connection = create_connection()
    try:
        with connection:
            connection.execute("INSERT INTO data (Name,GamesPlayed, Wins, Loss, Draw)VALUES (?,?,?,?,?)",(Name,GamesPlayed, Wins,Loss,Draw))


    except Exception as e:
        print(f"Error: {e}")
def show_data():
    connection = create_connection()
    try:
        with connection:
            df = pd.read_sql("SELECT * FROM data",connection)
            print(df.to_string(index=None))
    except Exception as e:
        print(f"Error: {e}")

def delete_data(id):
    connection = create_connection()
    try:
        with connection:
            connection.execute("DELETE FROM data WHERE rowid = (?)",id)
            connection.execute(
                "UPDATE data SET playerId = playerId - 1 WHERE playerId > ?",
                (id,))
    except Exception as e:
        print(f"Error: {e}")

def update_data(gamesPlayed,wins,loss,draw):
    connection = create_connection()
    try:
        with connection:
            connection.execute("""
                UPDATE data
                SET Wins = ?,
                    GamesPlayed = ?,
                    Loss = ?,
                    Draw = ?
                WHERE rowid = (SELECT MAX(rowid) FROM data)
            """, (wins, gamesPlayed, loss, draw))

    except Exception as e:
        print(f"Error: {e}")
