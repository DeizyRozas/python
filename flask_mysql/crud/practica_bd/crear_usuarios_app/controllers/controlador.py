
from flask import Flask, render_template, redirect, request
from crear_usuarios_app import app
from crear_usuarios_app.models.usuarios import Usuario

@app.route("/")
def mostrar_usuarios():
    usuarios= Usuario.mostrar_usuarios()
    return render_template("index.html", usuarios=usuarios )


@app.route("/crear_usuario", methods=["POST"])
def crear_usuarios():
    data={
        "nombre": request.form["nombre"],
        "especie": request.form["especie"]
    }
    Usuario.crear_usuarios(data)
    return redirect("/")

@app.route("/crear")
def crear():
    return render_template("add_usuarios.html")


