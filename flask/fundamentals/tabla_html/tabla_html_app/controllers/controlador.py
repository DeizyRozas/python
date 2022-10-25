from tabla_html_app import app
from flask import Flask, render_template, redirect, request, session
app.secret_key = "chocolate"

@app.route("/")
def mostrar_datos():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    return render_template("index.html", users=users)
