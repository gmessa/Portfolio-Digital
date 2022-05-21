from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/projetos.html")
def projetos():
    return render_template("projetos.html")

@app.route("/contato.html")
def contato():
    return render_template("contato.html")
