from flask import Flask, render_template, redirect, request,session, flash
from pensamientos_app import app
from pensamientos_app.models.pensamientos_model import Pensamiento
from pensamientos_app.models.users_model import User
# from pensamientos_app.models.message_model import Message

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def render_register():
    return render_template("index.html")

@app.route("/create_user", methods=["POST"])
def register():
    
    
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
    

    user_id = User.register(data)
    session["user_id"]= user_id
    return redirect("/pensamientos")  
    


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
    return redirect("/pensamientos")

@app.route("/logout")
def logout():
    session.clear()

    return redirect('/')

@app.route("/pensamientos")
def thoughts():
    if 'user_id' not in session:
        return redirect('/')

    data_user = {
        "user_id":session["user_id"]
    }
    #para guardar los datos del usuario en la session
    user_login=User.select_logged_user(data_user)
    all_thoughts= Pensamiento.show_thought()
    
    return render_template("pensamientos.html", user_login=user_login, all_thoughts=all_thoughts)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        "user_id":user_id
    }
    data_user = {
        "user_id":session["user_id"]
    }

    user=User.get_user_by_id(data)
    user_login=User.select_logged_user(data_user)
    all_thoughts = Pensamiento.show_thought_user(data)
    return render_template("users.html", user=user, user_login=user_login, all_thoughts=all_thoughts)