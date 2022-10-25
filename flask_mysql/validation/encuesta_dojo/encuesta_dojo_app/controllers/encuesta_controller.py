from flask import Flask, render_template, redirect, request,session, flash
from encuesta_dojo_app import app
from encuesta_dojo_app.models.encuesta_model import Encuesta


@app.route("/subir_info", methods=["POST"])
def subir_info():
    data={
        "nombre":request.form["nombre"],
        "ubicacion":request.form["ubicacion"],
        "idioma":request.form["idioma"],
        "comentario":request.form["comentario"]
    }
    info=Encuesta.subir_info(data)
    return redirect ("/mostrar_info")



@app.route("/")
def info():
    return render_template("index.html" )

@app.route("/mostrar_info")
def mostrar_info():
    dojos=Encuesta.mostrar_info()
    return render_template("result.html", dojos=dojos)