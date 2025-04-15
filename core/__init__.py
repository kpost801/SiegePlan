from flask import Flask
from core import models
from core.extensions import db, migrate
from core.routes.web import web
import os


def create_app(environment="production"):
	app = Flask(__name__)

	app.secret_key = '00858b3b6ada177a3cdf1035462fc7c5c4328ac2657ef1ea47b76fbff55b6b67'

	
	app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	app.config["DEBUG"] = environment == "development"

	# Initialize extensions
	db.init_app(app)

	# Register blueprints
	app.register_blueprint(web)  

	
	migrate.init_app(app, db)

     

	return app