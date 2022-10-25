from flask import Flask, render_template, redirect, request,session, flash
from recetas_app import app
from recetas_app.models.usuarios_modelo import Usuario
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def crear_user():
    return render_template("index.html")

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = { 
        "email" : request.form["email"] }
    usuario_en_db = Usuario.iniciar_sesion(data)
    # usuario no está registrado en la base de datos
    if usuario_en_db:
        flash(" Este Email ya esta registrado", 'registro')
        return redirect("/")

    if not Usuario.validacion(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email":request.form["email"],
        "password":pw_hash
    }

    usuario_id = Usuario.crear_usuario(data)
    session["usuario_id"]= usuario_id
    return redirect("/recetas")    


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    # ver si el nombre de usuario proporcionado existe en la base de datos
    data = { 
        "email" : request.form["email"] }
    usuario_en_db = Usuario.iniciar_sesion(data)
    # usuario no está registrado en la base de datos
    if not usuario_en_db:
        flash(" Usuario no registrado", 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(usuario_en_db.password, request.form['password']):
        # si obtenemos False después de verificar la contraseña
        flash("Password incorrecto", 'login')
        return redirect('/')
    # si las contraseñas coinciden, configuramos el user_id en sesión
    session['usuario_id'] = usuario_en_db.id
    # ¡¡¡Nunca renderices en una post!!!
    return redirect("/recetas")

@app.route("/cerrar_sesion")
def cerrar_session():
    session.clear()

    return redirect('/')