
from dojos_y_ninjas_app.models.dojo_model import Dojo
from dojos_y_ninjas_app.models.ninja_model import Ninja
from dojos_y_ninjas_app import app
from flask import Flask, render_template, redirect, request,session

@app.route("/agregar_ninja")
def inicio():
    dojos=Dojo.mostrar_dojos()

    return render_template ("index.html", dojos=dojos)

@app.route("/agregar_ninja", methods=["POST"])
def crear_ninja():
    
    data={
    "dojo_id":request.form["dojo_id"],
    "nombre": request.form["nombre"],
    "apellido": request.form["apellido"],
    "edad": request.form["edad"]
    }

    ninja=Ninja.crear_ninja(data)

    return redirect("/")