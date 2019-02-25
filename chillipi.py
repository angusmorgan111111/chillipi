from flask import Flask, g, render_template
from flask_apscheduler import APScheduler

import database

app = Flask(__name__)
scheduler = APScheduler()
scheduler.api_enabled = True


@app.before_first_request
def setup():
    database.init(app)
    scheduler.init_app(app)
    scheduler.start()


@scheduler.task('interval', id='read_ph', seconds=1)
def read_ph():
    with app.app_context():
        database.add_reading()


@app.route("/")
def index():
    readings = database.get_readings(20)
    return render_template('index.html', title='Dashboard | chillipi',
            readings=readings)


@app.route("/settings")
def settings():
    return render_template('settings.html', title='Settings | chillipi')


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()
