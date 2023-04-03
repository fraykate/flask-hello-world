import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# test the database connection
@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://kfray_renderapp_db_user:xm98rBz6dnCzMowhUlPPe97XI6KPJxlp@dpg-cglfedseoogkndgcqiag-a.oregon-postgres.render.com/kfray_renderapp_db")
    conn.close()
    return "Successful connection to kfray_renderapp_db database"

# create a table in the database
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