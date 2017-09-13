from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/members'
#app.config['SECRET_KEY'] = "password"
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'members'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


db = SQLAlchemy(app)

class Members(db.Model):
    __tablename__ = 'member_table'
    id = db.Column('member_id', db.Integer, primary_key=True)
    firstname = db.Column('firstname', db.String(255))
    surname = db.Column('surname', db.String(255))
    city = db.Column('city', db.String(255))
    addr = db.Column('addr', db.String(255))
    sex = db.Column('sex', db.String(255))
    phone = db.Column('phone', db.String(255))


def __init__(self, firstname, surname, city, addr, sex, phone):
    self.firstname = firstname
    self.surname = surname
    self.city = city
    self.addr = addr
    self.sex = sex
    self.phone = phone


@app.route('/')
def show_all():
    return render_template('show_all.html', Members=Members.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['firstname'] or not request.form['surname'] or not request.form['city']\
                or not request.form['addr'] or not request.form['sex']:
            flash('Please enter all the fields', 'error')
        else:
            member = Members(request.form['firstname'], request.form['surname'],
                             request.form['city'],request.form['addr'], request.form['sex'], request.form['phone'])

            db.session.add(member)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)



"""
engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(Department, backref=backref('employees', uselist=True, cascade='delete,all'))

    """



"""
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    #Connects to the specific database.
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    #Initializes the database.
    init_db()
    print('Initialized the database.')


def get_db():
    #Opens a new database connection if there is none yet for the current application context.

    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    #Closes the database again at the end of the request.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

"""





