from flask import Flask,render_template,redirect,request,session
from burgers_app import app
from burgers_app.models.burger_model import Burger
from burgers_app.models.topping import Topping
from burgers_app.models.users import User

@app.route('/create_burger')
def index():

    if 'user_id' not in session:
        return redirect('/')
    return render_template("index.html")

@app.route('/create',methods=['POST'])
def create():
    if not Burger.validate_burger(request.form):
        return redirect('/create_burger')
    data = {
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        "user_id": request.form['user_id']
    }
    if 'user_id' not in session:
        return redirect('/')

    Burger.save(data)
    return redirect('/burgers')

@app.route('/burgers')
def burgers():
    if 'user_id' not in session:
        return redirect('/')

    return render_template("results.html",all_burgers=Burger.get_all())


@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {
        'id': burger_id
    }
    if 'user_id' not in session:
        return redirect('/')
    return render_template("details_page.html",burger=Burger.get_one(data))

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    if 'user_id' not in session:
        return redirect('/')
    return render_template("edit_page.html", burger = Burger.get_one(data))

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data_hamburguesa = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    data_topping= {
        "burger_id": request.form['burger_id'],
        "topping_name": request.form['topping_name']
    }
    Burger.update(data_hamburguesa)
    topping_id= Topping.save(data_topping)
    data_muchos_a_muchos={
        "topping_id": topping_id,
        "burger_id": burger_id
    }
    Topping.agregar_toppings_a_hamburguesas(data_muchos_a_muchos)
    if 'user_id' not in session:
        return redirect('/')
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    if 'user_id' not in session:
        return redirect('/')
    Burger.destroy(data)
    return redirect('/burgers')