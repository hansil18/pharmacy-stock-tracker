import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgres://zrrzdqtlheepde:89cdf89f507190dc9bb3596cf4c0ac55993299eda8393dab4fd9666131bdd783@ec2-52-204-232-46.compute-1.amazonaws.com:5432/dbkdedb13nvri6")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
