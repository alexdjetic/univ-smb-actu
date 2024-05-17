from flask import Flask, redirect, url_for, request
from flask import render_template
from dataparser import DataParser
from managejson import ManageJson
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


@app.route("/")
def index():
    events: list = get_event()
    commentaires: list = get_comment()
    return render_template("index.html", events=events, commentaires=commentaires)


@app.route("/actualite")
def actualite():
    events: list = get_event()
    commentaires: list = get_comment()  
    return render_template("index.html", events=events, commentaires=commentaires)


@app.route("/concerts")
def concerts():
    events: list = get_event("Concerts")
    commentaires: list = get_comment()  
    return render_template("concerts.html", events=events, commentaires=commentaires)


@app.route("/rock")
def Rock():
    events: list = get_event("Rock")
    commentaires: list = get_comment()  
    return render_template("rock.html", events=events, commentaires=commentaires)


@app.route("/jazz")
def jazz():
    events: list = get_event("Jazz")
    commentaires: list = get_comment() 
    return render_template("jazz.html", events=events, commentaires=commentaires)

@app.route("/electro")
def electro():
    events: list = get_event("Electro")
    commentaires: list = get_comment() 
    return render_template("electro.html", events=events, commentaires=commentaires)


@app.route("/commentaire", methods=["GET", "POST"])
def commentaire():
    if request.method == "POST":
        managejson: ManageJson = ManageJson(f"{os.getcwd()}/static/commentaire.json")
            
        managejson.append({
            "nom": request.form['nom'],
            "commentaire": request.form['commentaire']
        })

        return redirect(url_for('actualite'))
