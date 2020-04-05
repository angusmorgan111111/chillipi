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


def get_readings(limit):
    db = get_db()
    c = db.cursor()

    return c.execute('''select time, ph, ec, tds from readings
        order by time desc limit ?''', (limit,))


def add_reading(ph, ec, tds):
    time = datetime.datetime.now()
    db = get_db()
    c = db.cursor()

    c.execute('''insert into readings
        values(?, ?, ?, ?)''', (time, ph, ec, tds))

    db.commit()


def get_schedule(output):
    db = get_db()
    c = db.cursor()

    return c.execute('''select day, time, command from output_schedule
        where output=? order by day asc, time asc''', (output,))


def get_pin(output):
    db = get_db()
    c = db.cursor()

    return c.execute('''select pin from output_mappings where output=?''', (output,)).fetchone()['pin']


def init(app):
    with app.app_context():
        db = get_db()

        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())

        db.commit()
