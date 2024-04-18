from flask import Flask
from flask_migrate import Migrate

from models import db, Users, Authenticate, Products

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def hello():
    return f"<h1>Let's Gooooooo!</h1>"


if __name__ == '__main__':
    app.run(port=5555, debug=True)