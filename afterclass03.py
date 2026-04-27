# import necessary libraries
import sqlite3
import pandas as pd

# connect with sqlite database
database = 'basketball.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

# read SQL query for getting all the tables of database into a dataframe
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)

# printing all the tables
print(tables)
print("------------------------------")

# print  the table team and analyse its fields
team = pd.read_sql("""SELECT * 
                    FROM Team;""", conn)

print(team)
print("------------------------------")

team.info()
print("------------------------------")

# top 10 nba teams that drafted the most number of players from university
draft = pd.read_sql("""SELECT * 
                    FROM Draft;""", conn)

draft.info()
print("------------------------------")

most_drafted = pd.read_sql("""
                            SELECT nameTeam, COUNT(DISTINCT idPlayer) AS total_players
                            FROM Draft
                            GROUP BY nameTeam
                            ORDER BY total_players DESC
                            LIMIT 10;
""", conn)

print(most_drafted)
