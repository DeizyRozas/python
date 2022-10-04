
from flask import Flask, render_template, request, redirect
from carpeta_app import app

@app.route('/lists')
def render_lists():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    estudiantes_info = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template("lists.html", random_numbers = [3,1,5], estudiantes = estudiantes_info)

@app.route('/')
def hola_mundo():
    return "Hola Mundo!!"


@app.route('/dojo')
def dojo():
    return "DOJO!"

@app.route('/say/<nombre>')
def say(nombre):
    return "Hola, " + nombre + "!"

@app.route('/repeat/<palabra>/<int:num>')       #que la palabra salga escrita las veces que escriba en numero
def repeat(palabra, num):
    return f"{palabra * num}"

# nuestra ruta de índice manejará la representación de nuestro formulario
@app.route('/registro')
def inicio_registro():
    return render_template("form.html")

@app.route('/users', methods=['POST'])
def crear_usuario():
    print("info posteada")
    name = request.form['name']
    email = request.form['email']
    print (name)
    return redirect("/show")	 
    
# agregar este método
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")

@app.errorhandler(404)
def page_not_found(e):
    return"esta ruta no fue encontrada"