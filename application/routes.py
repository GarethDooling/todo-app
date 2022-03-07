from application import app, db
from application.models import Teams
from application.forms import CreateForm, UpdateForm
from flask import render_template, redirect, url_for, request

@app.route('/create', methods=['GET', 'POST'])
def create():
    createform = CreateForm()

    if createform.validate_on_submit():
        team = Teams(name=createform.name.data)
        db.session.add(team)
        db.session.commit()

        return redirect(url_for('read'))
    return render_template('create.html', form=createform)

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    teams = Teams.query.all()
    return render_template('read.html', teams=teams)

@app.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    updateform = UpdateForm()
    team = Teams.query.filter_by(name=name).first()

    if request.method == 'GET':
        updateform.name.data = team.name
        return render_template('update.html', form=updateform)    
  
    else:
        if updateform.validate_on_submit():
            team.name = updateform.name.data
            db.session.commit()
            return redirect(url_for('read'))

@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete(name):
    team = Teams.query.filter_by(name=name).first()
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('read'))

# @app.route('/create/team')
# def create_team():
#     new_team = Teams(name="New Team")
#     db.session.add(new_team)
#     db.session.commit()
#     return f"Team {new_team.id} added to database"

# @app.route('/read/allTeams')
# def read_teams():
#     all_teams = Teams.query.all()

#     teams_dict = {"teams": []}

#     for team in all_teams:
#         teams_dict["teams"].append(
#             {
#                 "name": team.name
#             }
#         )

#     return teams_dict

# @app.route('/update/team/<int:id>/<new_name>')
# def update_team(id, new_name):
#     team = Teams.query.get(id)
#     team.name = new_name
#     db.session.commit()
#     return f"Team {id} updated to {new_name}"

# @app.route('/delete/team/<int:id>')
# def delete_team(id):
#     team = Teams.query.get(id)
#     db.session.delete(team)
#     db.session.commit()
#     return f"Team {id} is deleted"