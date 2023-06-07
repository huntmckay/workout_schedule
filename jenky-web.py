import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://admin:p0stdev@0.0.0.0"
# init the app with the extension
db.init_app(app)

class Strength(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    exerise = db.Column(db.String, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

class Endurance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    exerise = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    distance = db.Column(db.Integer, nullable=False)

class Flexibility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    exerise = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return 'Index Page'

# for more queries https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/
@app.route("/strength")
def strength_exercise_list():
    exercises = db.session.execute(db.select(Strength).order_by(Strength.date)).scalars()
    return render_template("strength/list.html", strength=strength)

@app.route("/strength/create", methods=["GET", "POST"])
def strength_create():
    if request.method == "POST":
        strength = Strength(
            date        = datetime.datetime.now(), # TODO I should let the db decide datetime
            exercise    = request.form["exercise"], 
            sets        = request.form["sets"],
            reps        = request.form["reps"],
            weight      = request.form["weight"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("strength_detail", id=strength.id))

    return render_template("strength/create.html")

@app.route("/strength/<int:id>")
def strength_detail(id):
    strength = db.get_or_404(Strength, id)

    return render_template("strength/detail.html", strength=strength)

@app.route("/strength/<int:id>/delete", methods=["GET", "POST"])
def strength_delete(id):
    strength = db.get_or_404(Strength, id)
    if request.method == "POST":
        db.session.delete(strength)
        db.session.commit()
        return redirect(url_for("strength_list"))
    
    return render_template("strength/detail.html", strength=strength)
