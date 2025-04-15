from flask_sqlalchemy import SQLAlchemy
from core.extensions import db



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    rank = db.Column(db.String(50))
    role = db.Column(db.String(20))  # 'attacker' or 'defender'
    strategies = db.relationship('Project', backref='user')

class Project(db.Model):
        __tablename__ = "Project"
        id = db.Column(db.Integer, primary_key=True)
        project = db.Column(db.String(100), nullable=False)
        map = db.Column(db.String(100), nullable=False)
        role = db.Column(db.String(20))
        characters = db.Column(db.PickleType, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
        notes = db.Column(db.Text, nullable=True)