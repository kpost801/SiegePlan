from flask import Flask
from core.extensions import db
from core import models
from core.extensions import db, login_manager, migrate
from core.routes.web import web
import os
from dotenv import load_dotenv


def create_app(environment="production"):
	app = Flask(__name__)

	# Load configurations based on the environment
	app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	app.config["DEBUG"] = environment == "development"

	# Initialize extensions
	db.init_app(app)

	login_manager.init_app(app)
	login_manager.login_view = "auth.login"

	from core.routes.auth import auth
	from core.routes.web import web
	
	app.register_blueprint(web)
	app.register_blueprint(auth)


	migrate.init_app(app, db)

	
	

	return app