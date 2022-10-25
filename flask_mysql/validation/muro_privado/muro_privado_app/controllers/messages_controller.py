from flask import Flask, render_template, redirect, request,session, flash
from muro_privado_app import app
from muro_privado_app.models.message_model import Message


@app.route("/create/message", methods=["POST"])
def create_message():
    data={
        "message":request.form["message"],
        "user_sender_id" : request.form["user_sender_id"],
        "user_reciever_id" : request.form["user_reciever_id"]
    }
    message=Message.create_message(data)
    
    return redirect("/wall")
