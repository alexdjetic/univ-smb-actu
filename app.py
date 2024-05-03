from flask import Flask, redirect, url_for, request
from flask import render_template
from dataparser import DataParser
from managejson import ManageJson
import os


app = Flask(__name__)


@app.route("/")
def index():
    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/data.json")
    dataparser.extract()
    events: list = dataparser.extract_type()

    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/commentaire.json")
    dataparser.extract()
    commentaires: list = dataparser.extract_type()
    return render_template("index.html", events=events, commentaires=commentaires)


@app.route("/actualite")
def actualite():
    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/data.json")
    dataparser.extract()
    events: list = dataparser.extract_type()

    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/commentaire.json")
    dataparser.extract()
    commentaires: list = dataparser.extract_type()
    return render_template("index.html", events=events, commentaires=commentaires)


@app.route("/concerts")
def concerts():
    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/data.json")
    dataparser.extract()
    events: list = dataparser.extract_type("Concerts")

    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/commentaire.json")
    dataparser.extract()
    commentaires: list = dataparser.extract_type()
    return render_template("concerts.html", events=events, commentaires=commentaires)


@app.route("/rock")
def Rock():
    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/data.json")
    dataparser.extract()
    events: list = dataparser.extract_type("Rock")

    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/commentaire.json")
    dataparser.extract()
    commentaires: list = dataparser.extract_type()
    return render_template("rock.html", events=events, commentaires=commentaires)


@app.route("/jazz")
def jazz():
    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/data.json")
    dataparser.extract()
    events: list = dataparser.extract_type("Jazz")

    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/commentaire.json")
    dataparser.extract()
    commentaires: list = dataparser.extract_type()
    return render_template("jazz.html", events=events, commentaires=commentaires)

@app.route("/electro")
def electro():
    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/data.json")
    dataparser.extract()
    events: list = dataparser.extract_type("Electro")

    dataparser: DataParser = DataParser(f"{os.getcwd()}/static/commentaire.json")
    dataparser.extract()
    commentaires: list = dataparser.extract_type()
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