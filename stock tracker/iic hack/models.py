from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Login(db.Model):
    __tablename__ = "logins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String,nullable=False)


class Medicine(db.Model):
    __tablename__ = "medicines"
    id=db.Column(db.Integer, primary_key=True)
    avail = db.Column(db.String, nullable=False)
    mname = db.Column(db.String, nullable=False)
    shopid = db.Column(db.Integer,db.ForeignKey("logins.id"), nullable=False)
