from flask import Flask, g, render_template
from flask_apscheduler import APScheduler

import database, output_scheduler, sensor, util, datetime, web_settings

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


@scheduler.task('interval', id='apply_schedule', seconds=1)
def apply_schedule():
    with app.app_context():
        for entry in database.get_outputs():
            
            pin = entry['pin']
            output = entry['output']
           
            if isinstance(pin, int):
                schedule = database.get_schedule(output)
                #util.log_iterable(schedule)
                #util.log('output '+ str(output))
                #util.log('pin ' + str(pin))
                output_scheduler.apply_outputs(schedule, pin)
        
       
@app.route("/")
def index():
    readings = database.get_readings(10)
    return render_template('index.html', title='Dashboard | chillipi', readings=readings)


@app.route("/settings/change_name/<output_number>", methods=['POST'])
def change_name(output_number):
    web_settings.change_name(output_number)
    
    return settings()


@app.route("/settings/add_command/<output_number>", methods=['POST'])
def add_command(output_number):
    
    for day in range (0, 7):
        web_settings.add_command(day, output_number)
   
    for day in range (0, 7):
        web_settings.clear_commands(day, output_number)
    
        
    
    return settings()




@app.route("/settings")
def settings():
     
    outputs = database.get_outputs()
        
    schedule = database.get_schedule_all()
    
    yesterday = (datetime.datetime.now().weekday()-1) % 7
       
    
    return render_template('settings.html', title='Settings | chillipi', outputs=outputs, schedule=schedule, yesterday=yesterday)



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()

