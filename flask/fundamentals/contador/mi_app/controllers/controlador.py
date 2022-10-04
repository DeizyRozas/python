from mi_app import app
from flask import Flask, render_template, redirect, request, session
app.secret_key = "chocolate"

@app.route("/")
def visitas_inicio():
    if "num" in session:
        session["num"]+=1
    
    else:
        session["num"] =1

    return render_template("index.html")

@app.route("/contador2")
def contador2():
    session["num"]+=1
    return redirect("/")

@app.route("/eliminar")
def eliminar():
    session.clear()
    return redirect ("/")
