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

# rows with null values in column
draft = pd.read_sql("""SELECT * 
                    FROM Draft;""", conn)

draft.info()
print("------------------------------")

null_values = pd.read_sql("""SELECT * 
                         FROM Draft
                         WHERE nameOrganizationFrom IS NULL;""", conn)

# printing
print(null_values)
print("------------------------------")

# found earliest
team = pd.read_sql("""
                           SELECT *
                           FROM Team;
                           """, conn)

print(team.info())
print("------------------------------")

earliest = pd.read_sql("""
                           SELECT *
                           FROM Team
                           ORDER BY year_founded;
                           """, conn)

print(earliest.head())

# found latest
latest = pd.read_sql("""
                           SELECT *
                           FROM Team
                           ORDER BY year_founded DESC;
                           """, conn)

print(latest.head())