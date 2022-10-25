from flask import Flask, render_template, redirect, request,session, flash
from dojos_y_ninjas_app import app
from dojos_y_ninjas_app.models.dojo_model import Dojo
from dojos_y_ninjas_app.models.ninja_model import Ninja

@app.route("/")
def mostrar_crear_dojo():
    dojos=Dojo.mostrar_dojos()
    return render_template ("dojos.html", dojos=dojos)

@app.route("/crear_dojo", methods=["POST"])
def crear_dojo():
    data={
        "nombre":request.form["nombre"]
    }

    dojo= Dojo.crear_dojo(data)
    
    return redirect("/")

@app.route("/dojos/<int:id>")
def mostrar_dojo(id):
    data={
        "id":id
    }
    dojo=Dojo.un_dojo(data)
    ninjas=Ninja.ninjas_por_dojo(data)
    return render_template("dojo_show.html", dojo=dojo, ninjas=ninjas)
