from flask import Blueprint, render_template
from flask_login import current_user, login_required
web = Blueprint("web", __name__)

@web.route("/")
def home():
	return render_template("index.html", user=current_user)

@web.route("/dashboard")
@login_required
def dashboard():
   return render_template("index.html", user=current_user)

@web.route("/project")
def project():
	return render_template("project.html")