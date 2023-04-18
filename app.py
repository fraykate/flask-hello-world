#####
#####
# Author: Kate Fray
# Updated: 4/17/2023 with commentary
# Description: This file is an application that uses route methods to create, test, populate, teardown and display data from a postgres database
# Use Case: This can be used as a base file for building applications that need to interact with databases.
#####
#####

import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Test the database connection:
# This route connects to the intended database
# closes the db connection
# and returns a 'success' message
@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://kfray_renderapp_db_user:xm98rBz6dnCzMowhUlPPe97XI6KPJxlp@dpg-cglfedseoogkndgcqiag-a.oregon-postgres.render.com/kfray_renderapp_db")
    conn.close()
    return "Successful connection to kfray_renderapp_db database"

# Create a table in the database:
# This route connects to the database
# exeutes a 'CREATE TABLE' command to create the Basketball table with specified metadata
# commits the change, closes the db connection
# and returns a 'success' message.
@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgres://kfray_renderapp_db_user:xm98rBz6dnCzMowhUlPPe97XI6KPJxlp@dpg-cglfedseoogkndgcqiag-a.oregon-postgres.render.com/kfray_renderapp_db") 
    # create a cursor
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return "Successfully created Basketball table"

# Insert values into the table
@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgres://kfray_renderapp_db_user:xm98rBz6dnCzMowhUlPPe97XI6KPJxlp@dpg-cglfedseoogkndgcqiag-a.oregon-postgres.render.com/kfray_renderapp_db") 
    # create a cursor
    c = conn.cursor()
    c.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Successfully populated Basketball table"

# Query all of the data in the database and return data in a table format
@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgres://kfray_renderapp_db_user:xm98rBz6dnCzMowhUlPPe97XI6KPJxlp@dpg-cglfedseoogkndgcqiag-a.oregon-postgres.render.com/kfray_renderapp_db") 
    c = conn.cursor()
    # Query the table and store in records
    c.execute('''
        SELECT * FROM Basketball;
        ''')
    records = c.fetchall()
    conn.close()
    # HTML formatting for results
    response = ""
    response += "<table>"
    for player in records:
        response += "<tr>"
        for info in player:
            response += "<td>{}</td>".format(info)
        response += "</tr>"
    response += "</table>"
    return response

# Drop the Basketball table from the database
@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgres://kfray_renderapp_db_user:xm98rBz6dnCzMowhUlPPe97XI6KPJxlp@dpg-cglfedseoogkndgcqiag-a.oregon-postgres.render.com/kfray_renderapp_db") 
    c = conn.cursor()
    c.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Successfully dropped Basketball table"
