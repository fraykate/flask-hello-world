import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/db_test')
def db_test:
    conn = psycopg2.connect("postgres://kfray_renderapp_db_user:xm98rBz6dnCzMowhUlPPe97XI6KPJxlp@dpg-cglfedseoogkndgcqiag-a.oregon-postgres.render.com/kfray_renderapp_db")
    conn.close()
    return "Successful connection to kfray_renderapp_db database"

@app.route('/')
def hello_world():
    return 'Hello, World!'
