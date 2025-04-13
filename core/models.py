from flask_sqlalchemy import SQLAlchemy
from core.extensions import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from core import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    rank = db.Column(db.String(50))
    role = db.Column(db.String(20))  # 'attacker' or 'defender'
    strategies = db.relationship('Strategy', backref='author', lazy=True)

    def set_password(self, password):
                self.password = generate_password_hash(
                password, method="pbkdf2:sha256", salt_length=16
                )

    def check_password(self, password):
          return check_password_hash(self.password, password)

class Map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class Operator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20))  # 'attacker' or 'defender'
    speed = db.Column(db.Integer)
    armor = db.Column(db.Integer)
    ability_description = db.Column(db.Text)

class Strategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    map_id = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False)
    site = db.Column(db.String(100))
    role = db.Column(db.String(10))  # 'attack' or 'defense'
    description = db.Column(db.Text)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # map = db.relationship('Map', backref='strategies')
    # operators = db.relationship('Operator', secondary=strategy_operators, backref='strategies')

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
