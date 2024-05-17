from flask import Flask, redirect, url_for, request, session
from flask import render_template
from dataparser import DataParser
from managejson import ManageJson
from random import randint
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
    islogin: bool = True if len(session) > 0 else False
    return render_template("index.html", events=events, commentaires=commentaires, login=islogin)


@app.route("/actualite", methods=["GET", "POST"])
def actualite():
    if request.method == "POST":
        managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/data.json")
            
        managejson.append({
            "type": "actualite",
            "date": request.form['date'],
            "titre": request.form['titre'],
            "description": request.form['desc'],
            "id": randint(50,50000)
        })

        return redirect(url_for('actualite'))

    events: list = get_event("actualite")
    commentaires: list = get_comment()
    islogin: bool = True if len(session) > 0 else False  
    return render_template("index.html", events=events, commentaires=commentaires, login=islogin)


@app.route("/add_concerts")
def add_concerts():
    if not session.get("user", "") and not session.get("password", ""):
        return redirect(url_for('actualite'))

    islogin: bool = True if len(session) > 0 else False
    return render_template("add_concerts.html", login=islogin)


@app.route("/add_actualite")
def add_actualite():
    if not session.get("user", "") and not session.get("password", ""):
        return redirect(url_for('actualite'))

    islogin: bool = True if len(session) > 0 else False
    return render_template("add_actualite.html", login=islogin)


@app.route("/concerts", methods=["GET", "POST"])
def concerts():
    if request.method == "POST":
        managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/data.json")
            
        managejson.append({
            "type": "Concerts",
            "date": request.form['date'],
            "titre": request.form['titre'],
            "description": request.form['desc'],
            "id": randint(50,50000)
        })

        return redirect(url_for('concerts'))

    events: list = get_event("Concerts")
    commentaires: list = get_comment()
    islogin: bool = True if len(session) > 0 else False 
    return render_template("concerts.html", events=events, commentaires=commentaires, login=islogin)


@app.route("/rock")
def Rock():
    events: list = get_event("Rock")
    commentaires: list = get_comment()
    islogin: bool = True if len(session) > 0 else False  
    return render_template("rock.html", events=events, commentaires=commentaires, login=islogin)


@app.route("/jazz")
def jazz():
    events: list = get_event("Jazz")
    commentaires: list = get_comment()
    islogin: bool = True if len(session) > 0 else False 
    return render_template("jazz.html", events=events, commentaires=commentaires, login=islogin)

@app.route("/electro")
def electro():
    events: list = get_event("Electro")
    commentaires: list = get_comment()
    islogin: bool = True if len(session) != 0 else False 
    return render_template("electro.html", events=events, commentaires=commentaires, login=islogin)


@app.route("/commentaire", methods=["GET", "POST"])
def commentaire():
    if request.method == "POST":
        managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/commentaire.json")
            
        managejson.append({
            "nom": request.form['nom'],
            "commentaire": request.form['commentaire']
        })

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
        return redirect(url_for('actualite'))

    if not request.args.get('id'):
        return redirect(url_for('actualite'))

    print(f"id: {request.args.get('id')}")
    print(f"type: {type(int(request.args.get('id')))}")

    managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/data.json")
    result: bool = managejson.delete_ligne(int(request.args.get('id')))
    # return redirect(url_for('actualite'))
    return f"Supprésion de de l'évènement ayant l'identifant {request.args.get('id')}({type(int(request.args.get('id')))}):\nrésultat: {result}"
