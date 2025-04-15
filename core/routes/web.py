from flask import Blueprint, render_template, request, redirect, url_for, session
from core.models import Project, db
web = Blueprint("web", __name__)

@web.route("/")
def home():
	recent_strategies = Project.query.order_by(Project.id.desc()).limit(5).all()
	return render_template("index.html", recent_strategies=recent_strategies)



@web.route("/project",methods=["GET", "POST"])
def project():
	if request.method == "POST":
		project = request.form.get("project")
		map = request.form.get("map")
		role = request.form.get("role")
		characters = request.form.getlist("characters[]")
		new_strategy = Project(
            project =project,
            map=map,
            role=role,
            characters=",".join(characters)
        )
		db.session.add(new_strategy)
		db.session.commit()
		
		session['strategies'] = [{
			'id': new_strategy.id,
			'project_name': new_strategy.project,
            'map': new_strategy.map,
            'role': new_strategy.role,
            'characters': new_strategy.characters
        }]
		
		return redirect(url_for("web.strat"))
	
	strategies = Project.query.all()
	return render_template("project.html",strategies=strategies)

@web.route('/strat')
def strat():
    strategies = session.get('strategies', [])
    
    map_image_paths = {
        "Bank": url_for('static', filename='pictures/bank2.jpeg'),
        "Border": url_for('static', filename='pictures/border2.jpeg.jpg'),
        "Chalet": url_for('static', filename='pictures/chalet2.jpeg'),
        "Clubhouse": url_for('static', filename='pictures/club2ndfloor.jpeg'),
        "Consulate": url_for('static', filename='pictures/cons2.jpeg'),
        "Kafe Dostoyevsky": url_for('static', filename='pictures/kafe2.jpeg'),
        "Nighthaven Labs": url_for('static', filename='pictures/labs2.jpeg'),
        "Oregon": url_for('static', filename='pictures/2ndfloodoregon.jpeg'),
        "Skyscraper": url_for('static', filename='pictures/sky2.jpeg'),
        "Theme Park": url_for('static', filename='pictures/theme2.jpeg'),
        "Villa": url_for('static', filename='pictures/villa2.jpeg'),
    }

    for strat in strategies:
        strat['mapImage'] = map_image_paths.get(strat['map'], '')

    return render_template('strat.html', strategies=strategies)

@web.route('/save_notes/<int:strategy_id>', methods=['POST'])
def save_notes(strategy_id):
    notes = request.form.get('notes')
    strategy = Project.query.get_or_404(strategy_id)
    strategy.notes = notes
    db.session.commit()
    return redirect(url_for('web.strat'))

@web.route('/delete_strategy/<int:strategy_id>', methods=['POST'])
def delete_strategy(strategy_id):
    strategy = Project.query.get_or_404(strategy_id)
    db.session.delete(strategy)
    db.session.commit()
    return redirect(url_for('web.home'))