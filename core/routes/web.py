from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from core.models import Project
web = Blueprint("web", __name__)
from core import db

@web.route("/")
def home():
	return render_template("index.html", user=current_user)

@web.route("/dashboard")
@login_required
def dashboard():
   return render_template("index.html", user=current_user)

@web.route("/project", methods=["GET", "POST"])
@login_required
def project():
    if request.method == "POST":
        name = request.form.get("project")
        map_choice = request.form.get("map")
        role = request.form.get("role")
        characters = request.form.getlist("characters[]")

        if len(characters) > 5:
            flash("You can only select up to 5 characters.", "danger")
            return redirect(url_for("web.project"))

        new_project = Project(
            name=name,
            map=map_choice,
            role=role,
            characters=characters,
            user=current_user
        )

        db.session.add(new_project)
        db.session.commit()
        flash("Project created successfully!", "success")
        return redirect(url_for("web.dashboard"))

    return render_template("project.html")