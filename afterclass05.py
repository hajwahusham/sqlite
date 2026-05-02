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
player = pd.read_sql("""SELECT * 
                    FROM Player;""", conn)

print(player)
print("------------------------------")

player.info()
print("------------------------------")

# print  the table player_salary and analyse its fields
Player_Salary = pd.read_sql("""SELECT * 
                    FROM Player_Salary;""", conn)

print(Player_Salary)
print("------------------------------")

Player_Salary.info()
print("------------------------------")

# display nameteam, nameplayer, and value of table player_salary and is_active of table player
P_Salary = pd.read_sql("""SELECT nameTeam, namePlayer, value 
                    FROM Player_Salary;""", conn)

print(P_Salary)
print("------------------------------")

is_active = pd.read_sql("""SELECT is_active
                    FROM Player;""", conn)

print(is_active)
print("------------------------------")

# join both tables based on team name

join = pd.read_sql("""SELECT *
                    FROM Player AS p
                    INNER JOIN Player_Salary AS ps
                    ON p.full_name = ps.namePlayer;""", conn)
print(join)
