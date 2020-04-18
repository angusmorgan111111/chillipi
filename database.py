import datetime, random, sqlite3
from flask import g

DATABASE = 'chilli.db'

def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = sqlite3.connect(DATABASE,
                detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def write_db(query, args=()):
    cur = get_db().execute(query, args)
    get_db().commit()
    cur.close()


def get_readings(limit):
    return query_db('''select time, ph, ec, tds from readings
        order by time desc limit ?''', (limit,))


def add_reading(ph, ec, tds):
    time = datetime.datetime.now()
    db = get_db()
    c = db.cursor()

    write_db('''insert into readings
        values(?, ?, ?, ?)''', (time, ph, ec, tds))


def get_schedule(output):
    return query_db('''select day, time, command from output_schedule
        where output=? order by day asc, time asc''', (output,))

def get_schedule_all():
    return query_db('''select day, time, command, output from output_schedule
        order by day asc, time asc''')


def get_pin(output):
    return query_db('''select pin from output_mappings where
        output=?''', (output,)).fetchone()['pin']


def get_outputs():
    return query_db('''select pin, output, name from output_mappings''')


def add_output(output, pin, name):
      write_db('''insert into output_mappings
        values(?, ?, ?)''', (output, pin, name))


def change_name(output_number, output_name):
        write_db('''UPDATE output_mappings
        SET name = ? 
        WHERE output = ?''', (output_name, output_number))




def init(app):
    with app.app_context():
        db = get_db()

        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
             
        db.commit()

        if not get_outputs():
            add_output(0, 20, '-')
            add_output(1, 21, '-')
            add_output(2, 20, '-')
            add_output(3, 21, '-')
            add_output(4, 20, '-')
            add_output(5, 20, '-')
        
            



        
