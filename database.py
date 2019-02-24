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

    return c.execute('''select time, ph from ph_readings
        order by time desc limit ?''', (limit,))


def add_reading():
    time = datetime.datetime.now()
    ph = round(random.uniform(0, 14), 1)
    db = get_db()
    c = db.cursor()

    c.execute('''insert into ph_readings
        values(?, ?)''', (time, ph))

    db.commit()


def init(app):
    with app.app_context():
        db = get_db()

        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())

        db.commit()
