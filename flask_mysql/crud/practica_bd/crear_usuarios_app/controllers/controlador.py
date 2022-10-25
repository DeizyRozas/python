from flask import Flask, render_template, redirect, request,session, flash
from crear_usuarios_app import app
from crear_usuarios_app.models.usuarios import Usuario
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/mostrar_usuarios")
def mostrar_usuarios():
    if 'usuario_id' not in session:
        return redirect('/inicio_sesion')
    usuarios= Usuario.mostrar_usuarios()
    return render_template("index.html", usuarios=usuarios )


@app.route("/crear_usuario", methods=["POST"])
def crear_usuarios():
    data = { 
        "correo_electronico" : request.form["correo_electronico"] }
    usuario_en_db = Usuario.iniciar_sesion(data)
    # usuario no está registrado en la base de datos
    if usuario_en_db:
        flash(" Este Email ya esta registrado", 'registro')
        return redirect("/inicio_sesion")

    if not Usuario.validacion(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['contraseña'])

    data={
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "correo_electronico":request.form["correo_electronico"],
        "contraseña":pw_hash
    }

    usuario_id = Usuario.crear_usuarios(data)
    session["usuario_id"]= usuario_id
    return redirect("/mostrar_usuarios")

@app.route("/")
def crear():
    return render_template("add_usuarios.html")

@app.route("/borrar/<int:usuario_id>")
def borrar(usuario_id):
    data = {
        'id': usuario_id,
    }
    if 'usuario_id' not in session:
        return redirect('/inicio_sesion')
    print (data["id"])
    Usuario.borrar(data)
    return redirect("/mostrar_usuarios")

@app.route("/actualizar/<int:usuario_id>", methods=["POST"])
def editar_usuario(usuario_id):
    if 'usuario_id' not in session:
        return redirect('/')
    data = {
        'id': usuario_id,
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "contraseña":request.form["contraseña"]
    }
    if not Usuario.validacion(request.form):
        return redirect('/')
    
    Usuario.editar(data)
    return redirect(f"/mostrar/{usuario_id}")

@app.route("/editar/<int:usuario_id>")
def editar(usuario_id):
    data={
        "id":usuario_id
    }
    if 'usuario_id' not in session:
        return redirect('/inicio_sesion')
    usuario = Usuario.mostrar_usuario(data)
    return render_template("editar_usuario.html",usuario=usuario)

@app.route("/mostrar/<int:usuario_id>")
def mostrar(usuario_id):
    data = {
        'id': usuario_id,
    }
    if 'usuario_id' not in session:
        return redirect('/inicio_sesion')
    usuario=Usuario.mostrar_usuario(data)
    return render_template ("mostrar.html", usuario=usuario)

@app.route("/inicio_sesion")
def inicio_sesion():
    return render_template("/add_usuarios.html")

@app.route("/cerrar_sesion")
def cerrar_session():
    session.clear()
    return redirect('/inicio_sesion')

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    # ver si el nombre de usuario proporcionado existe en la base de datos
    data = { 
        "correo_electronico" : request.form["correo_electronico"] }
    usuario_en_db = Usuario.iniciar_sesion(data)
    # usuario no está registrado en la base de datos
    if not usuario_en_db:
        flash(" Email/Contraseña invalida", 'login')
        return redirect("/inicio_sesion")
    if not bcrypt.check_password_hash(usuario_en_db.contraseña, request.form['contraseña']):
        # si obtenemos False después de verificar la contraseña
        flash("Email/Password invalida", 'login')
        return redirect('/inicio_sesion')
    # si las contraseñas coinciden, configuramos el user_id en sesión
    session['usuario_id'] = usuario_en_db.id
    # ¡¡¡Nunca renderices en una post!!!
    return redirect("/mostrar_usuarios")
