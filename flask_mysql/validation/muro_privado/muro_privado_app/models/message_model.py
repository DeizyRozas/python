from unittest import result
from muro_privado_app.config.mysqlconnection import connectToMySQL
from flask import flash
from muro_privado_app import app

class Message:
    def __init__(self,data):
        self.id = data['id']
        self.message = data['message']
        self.user_sender_id = data["user_sender_id"]
        self.user_reciever_id = data["user_reciever_id"]
        self.created_at = data["created_at"]
        self.updated_at= data["updated_at"]
        self.user=[]

    @classmethod
    def create_message(cls, data):
        query ="INSERT INTO messages (message, user_sender_id, user_reciever_id) VALUES (%(message)s, %(user_sender_id)s,  %(user_reciever_id)s);"
        result= connectToMySQL("muro_privado").query_db(query, data)
        return result

    @classmethod
    def display_messages_for_user_logged(cls,data):
        query = "select * from messages join users on users.id = messages.user_sender_id where messages.user_reciever_id= %(user_id)s;"
        results=connectToMySQL("muro_privado").query_db(query, data)
        messages_for_user_logged=[]
        for messages in results:
            messages_for_user_logged.append(cls(messages))
        return messages_for_user_logged

    