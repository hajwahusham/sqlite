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

# printing
print(tables)
print("------------------------------")

# print  the table team and analyse its fields
team = pd.read_sql("""SELECT * 
                    FROM Team;""", conn)

print(team)
print("------------------------------")

team.info()
print("------------------------------")

# print  the table team_attributes and analyse its fields
team_attri = pd.read_sql("""SELECT * 
                    FROM Team_Attributes;""", conn)

print(team_attri)
print("------------------------------")

team_attri.info()
print("------------------------------")

# display the details of the table team_attributes of teams that belong to the state new york
team_attri = pd.read_sql("""SELECT * 
                        FROM Team_Attributes
                        WHERE id IN (SELECT id 
                        FROM Team
                        WHERE City='New York') ;""", conn)

print(team_attri)
print("------------------------------")