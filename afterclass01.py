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