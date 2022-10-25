from dis import dis
from flask import Flask, render_template, redirect, request,session, flash
from muro_privado_app import app
from muro_privado_app.models.user_model import User
from muro_privado_app.models.message_model import Message

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def render_create_user():
    return render_template("index.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    
    
    if not User.validation(request.form):
        return redirect('/')

    data_comprobation = { 
        "email" : request.form["email"] 
    }
    user_in_db = User.login(data_comprobation)
    # usuario no está registrado en la base de datos
    if user_in_db:
        flash(" Este Email ya esta registrado", 'register')
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email":request.form["email"],
        "password":pw_hash
    }
    

    user_id = User.create_user(data)
    session["user_id"]= user_id
    return redirect("/wall")  
    


@app.route('/login', methods=['POST'])
def login():
    # ver si el nombre de usuario proporcionado existe en la base de datos
    data = { 
        "email" : request.form["email"] 
    }
    user_in_db = User.login(data)
    # usuario no está registrado en la base de datos
    if not user_in_db:
        flash(" Usuario no registrado", 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # si obtenemos False después de verificar la contraseña
        flash("Password incorrecto", 'login')
        return redirect('/')
    # si las contraseñas coinciden, configuramos el user_id en sesión
    session['user_id'] = user_in_db.id
    # ¡¡¡Nunca renderices en una post!!!
    return redirect("/wall")

@app.route("/wall")
def show_wall():
    if 'user_id' not in session:
        return redirect('/')

    data_user = {
        "user_id":session["user_id"]
    }
    print(session)
    #para guardar los datos del usuario en la session
    user_login=User.select_logged_user(data_user)
    all_users_in_db_except_logged=User.all_users_except_logged_user(data_user)
    display_messages= Message.display_messages_for_user_logged(data_user)
    user_sender=Message.user_sender(data_user)
    return render_template("wall.html", user_login=user_login, all_users_in_db_except_logged=all_users_in_db_except_logged, display_messages=display_messages, user_sender=user_sender)

@app.route("/logout")
def logout():
    session.clear()

    return redirect('/')