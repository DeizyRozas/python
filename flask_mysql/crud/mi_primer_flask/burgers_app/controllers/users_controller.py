from burgers_app.models.users import User
from burgers_app import app
from flask import Flask, render_template, redirect, request,session

@app.route("/")
def inicio():
    return render_template ("login_reg.html")

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data={
    "first_name": request.form["first_name"],
    "last_name": request.form["last_name"],
    "email": request.form["email"],
    "password": request.form["password"]
    }

    if not User.validate_user(request.form):
        return redirect('/')

    user_id=User.registro(data)
    session["user_id"]=user_id
    return redirect("/create_burger")

@app.route("/clear_session")
def limpiar_session():
    session.clear()
    return redirect('/')