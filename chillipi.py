from flask import Flask, g, render_template
from flask_apscheduler import APScheduler

import database, output_scheduler, sensor

app = Flask(__name__)
scheduler = APScheduler()
scheduler.api_enabled = True


@app.before_first_request
def setup():
    database.init(app)
    scheduler.init_app(app)
    scheduler.start()


@scheduler.task('interval', id='read_sensors', seconds=10)
def read_sensors():
    with app.app_context():
        ph = sensor.read_ph().rstrip('\x00')
        ec_all = sensor.read_ec().split(',')
        database.add_reading(ph, ec_all[0], ec_all[1])


@app.route("/schedule")
def schedule():
    with app.app_context():
        pin = database.get_pin(0)
        schedule = database.get_schedule(0)
        return output_scheduler.apply_outputs(schedule, pin)
        # return render_template('schedule.html', title='Schedule | chillipi', schedule=schedule)
        


@app.route("/")
def index():
    readings = database.get_readings(10)
    return render_template('index.html', title='Dashboard | chillipi', readings=readings)


@app.route("/settings")
def settings():
    return render_template('settings.html', title='Settings | chillipi')


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()
