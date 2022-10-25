from flask import Flask, render_template, redirect, request,session, flash
from pensamientos_app import app
from pensamientos_app.controllers.users_controller import thoughts
from pensamientos_app.models.pensamientos_model import Pensamiento



@app.route("/add_thought", methods=["POST"])
def create_thought():
    if 'user_id' not in session:
        return redirect('/')
    data={
        "content":request.form["content"],
        "user_id":session["user_id"]
    }
    if not Pensamiento.validation(request.form):
        return redirect('/pensamientos')
    thought=Pensamiento.add_thought(data)
    
    return redirect("/pensamientos")

@app.route("/delete/<int:id>")
def delete_thought(id):

    data = {
        'id': id
    }
    print (data)
    Pensamiento.delete_thought(data)
    return redirect("/pensamientos")

@app.route("/like/<int:id>")
def like_thought(id):
    data= {
        "pensamiento_id":id,
        "user_id":session["user_id"]
    }
    data_pensamientos={
        "pensamiento_id":id
    }

    like=Pensamiento.like_thought(data)
    likes=Pensamiento.show_likes(data_pensamientos)
    return redirect ("/pensamientos")