from recetas_app.models.recetas_modelo import Receta
from recetas_app.models.usuarios_modelo import Usuario
from recetas_app import app
from flask import Flask, render_template, redirect, request,session

@app.route("/recetas")
def mostrar_recetas():
    if 'usuario_id' not in session:
        return redirect('/')
    # recetas = Receta.obtener_recetas()
    data_usuario = {
        "usuario_id":session["usuario_id"]
    }
    #para guardar los datos del usuario en la session
    user_login=Usuario.seleccionar_usuario(data_usuario)
    
    todas_recetas_con_usuarios=Receta.obtener_recetas_con_usuarios()
    return render_template("recetas.html", user_login=user_login, todas_recetas_con_usuarios=todas_recetas_con_usuarios)

@app.route("/crear_recipe")
def crear_receta():
    return render_template("crear_receta.html")

@app.route("/crear_receta", methods=["POST"])
def diccionario_receta():
    data ={
        "name" : request.form["name"],
        "under" : request.form["under"],
        "description" : request.form ["description"],
        "instruction" : request.form ["instruction"],
        "date_made" : request.form ["date_made"], 
        "user_id" : request.form ["user_id"]
    }
    if not Receta.validacion(request.form):
        return redirect('/crear_recipe')
    receta_id=Receta.crear_receta(data)
    return redirect ("/recetas")

@app.route("/editar/receta/<int:id>")
def mostrar_editar_receta(id):
    if 'usuario_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    receta=Receta.get_one_recipe(data)
    
    return render_template("editar_receta.html", receta=receta)

@app.route("/editar/receta/<int:id>", methods=["POST"])
def editar_receta(id):
    data ={
        "id" : id,
        "name" : request.form["name"],
        "under" : request.form["under"],
        "description" : request.form ["description"],
        "instruction" : request.form ["instruction"],
        "date_made" : request.form ["date_made"]
    }
    
    if not Receta.validacion(request.form):
        return redirect(f'/editar/receta/{id}')

    receta=Receta.editar_receta(data)
    return redirect("/recetas")

@app.route("/eliminar/receta/<int:id>")
def eliminar_receta(id):
    data = {
        'id': id
    }
    
    if 'usuario_id' not in session:
        return redirect('/')
    Receta.eliminar_receta(data)
    return redirect("/recetas")

@app.route("/ver/receta/<int:id>")
def ver_receta(id):
    if "usuario_id" not in session:
        return redirect("/")

    data = {
        "id":id
    }
    datausuario={
        "usuario_id": session["usuario_id"]
    }
    user_login= Usuario.seleccionar_usuario(datausuario)
    una_receta=Receta.receta_de_un_usuario(data)

    return render_template("ver.html", una_receta=una_receta, user_login=user_login)