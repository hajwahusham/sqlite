# import necessary libraries
import sqlite3
import pandas as pd

# connect with sqlite database
database = 'basketball.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')
print("------------------------------")

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


# display full_name, nickname, city and year_founded of teams founded after 1990
founded90 = pd.read_sql("""SELECT full_name, nickname, city, year_founded 
                           FROM Team
                           WHERE year_founded > '1990';""", conn)

print(founded90)
print("------------------------------")

# display all the details of the teams that belong to texas or new york

states = pd.read_sql("""SELECT * 
                           FROM Team
                           WHERE state = 'Texas' OR state = 'New York';""", conn)

print(states)
print("------------------------------")

# teams with names beginning with los
los = pd.read_sql("""SELECT full_name 
                     FROM Team
                     WHERE full_name LIKE 'Los%';""", conn)

print(los)  
print("------------------------------")                   

# check names of teams that have been found earliest and latest
earliest = pd.read_sql("""SELECT full_name, year_founded
                          FROM Team
                          WHERE year_founded = (SELECT MIN(year_founded) FROM Team)
                                OR year_founded = (SELECT MAX(year_founded) FROM Team)
                          ORDER BY year_founded;""", conn)
print(earliest)
print("---------------end---------------") 
