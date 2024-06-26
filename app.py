from flask import Flask, redirect, url_for, request, session
from flask import render_template
from dataparser import DataParser
from managejson import ManageJson
from random import randint
from form_format import Event, Commentaire, User
import os


def get_comment() -> list:
    """Cette fonction permet d'obtenir les commentaires"""
    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/commentaire.json")
    dataparser.extract()

    return dataparser.extract_type()


def get_event(filter: str = "all") -> list:
    """Cette fonction permet d'obtenir les évènements"""
    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/data.json")
    dataparser.extract()
    
    return dataparser.extract_type(filter)


app = Flask(__name__)
app.secret_key = 'azerty123456789'


@app.route("/")
def index():
    events: list = get_event()
    commentaires: list = get_comment()
    form = Commentaire()
    islogin: bool = True if len(session) > 0 else False
    return render_template("index.html", events=events, commentaires=commentaires, login=islogin, form=form)


@app.route("/actualite", methods=["GET", "POST"])
def actualite():
    form = Event()
    if form.validate_on_submit():
        managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/data.json")
        managejson.append(commentaire={
            "type": "actualite",
            "date": form.date.data.strftime('%m/%d/%y'),
            "titre": form.titre.data,
            "description": form.description.data,
            "id": randint(50,50000)
        })
        return redirect(url_for('actualite'))

    events: list = get_event("actualite")
    commentaires: list = get_comment()
    commentaire_form = Commentaire()
    islogin: bool = True if len(session) > 0 else False  
    return render_template("index.html", events=events, commentaires=commentaires, login=islogin, form=commentaire_form)


@app.route("/add_concerts")
def add_concerts():
    if not session.get("user", "") and not session.get("password", ""):
        return redirect(url_for('login'))

    form = Event()
    islogin: bool = True if len(session) > 0 else False
    return render_template("add_concerts.html", login=islogin, form=form)


@app.route("/add_actualite")
def add_actualite():
    if not session.get("user", "") and not session.get("password", ""):
        return redirect(url_for('login'))

    form = Event()
    islogin: bool = True if len(session) > 0 else False
    return render_template("add_actualite.html", login=islogin, form=form)


@app.route("/concerts", methods=["GET", "POST"])
def concerts():
    form = Event()
    if form.validate_on_submit():
        managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/data.json")
        managejson.append(commentaire={
            "type": "Concerts",
            "date": form.date.data.strftime('%m/%d/%y'),
            "titre": form.titre.data,
            "description": form.description.data,
            "id": randint(50,50000)
        })
        return redirect(url_for('concerts'))

    events: list = get_event("Concerts")
    commentaires: list = get_comment()
    commentaire_form = Commentaire()
    islogin: bool = True if len(session) > 0 else False 
    return render_template("concerts.html", events=events, commentaires=commentaires, login=islogin, form=commentaire_form)


@app.route("/rock")
def rock():
    events: list = get_event("Rock")
    commentaires: list = get_comment()
    form = Commentaire()
    islogin: bool = True if len(session) > 0 else False  
    return render_template("rock.html", events=events, commentaires=commentaires, login=islogin, form=form)


@app.route("/jazz")
def jazz():
    events: list = get_event("Jazz")
    commentaires: list = get_comment()
    form = Commentaire()
    islogin: bool = True if len(session) > 0 else False 
    return render_template("jazz.html", events=events, commentaires=commentaires, login=islogin, form=form)


@app.route("/electro")
def electro():
    events: list = get_event("Electro")
    commentaires: list = get_comment()
    form = Commentaire()
    islogin: bool = True if len(session) != 0 else False 
    return render_template("electro.html", events=events, commentaires=commentaires, login=islogin, form=form)


@app.route("/commentaire", methods=["GET", "POST"])
def commentaire():
    form = Commentaire()
    if form.validate_on_submit():
        managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/commentaire.json")
        managejson.append(commentaire={
            "nom": form.nom.data,
            "commentaire": form.commentaire.data
        })
        return redirect(url_for('actualite'))

    return redirect(url_for('actualite'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if session.get("user", "NA") == "NA":
            session["user"] = request.form['user']
            session["password"] = request.form['password']
            return redirect(url_for('actualite'))
        else:
            return redirect(url_for('actualite'))
    else:
        islogin: bool = True if len(session) > 0 else False 
        return render_template("login.html", login=islogin)


@app.route("/logout", methods=["GET"])
def logout():
    if not session.get("user", "") and not session.get("password", ""):
        return redirect(url_for('actualite'))

    session.pop("user")
    session.pop("password")
    return redirect(url_for('actualite'))


@app.route("/delete", methods=["GET"])
def delete_event():
    if not session.get("user", "") and not session.get("password", ""):
        return redirect(url_for('login'))

    if not request.args.get('id'):
        return redirect(url_for('actualite'))

    managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/data.json")
    managejson.delete_ligne(int(request.args.get('id')))
    return redirect(url_for('actualite'))


if __name__ == "__main__":
    app.run(debug=True)
