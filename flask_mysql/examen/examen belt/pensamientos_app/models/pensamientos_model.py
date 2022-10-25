from pensamientos_app import app
from pensamientos_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pensamientos_app.models.users_model import User

class Pensamiento:
    def __init__(self,data):
        self.id = data['id']
        self.content =data ['content']
        self.user_id =data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at= data["updated_at"]
        self.users=[]


    @classmethod
    def add_thought(cls,data):
        query="INSERT INTO pensamientos (content, user_id) VALUES (%(content)s, %(user_id)s );"
        result = connectToMySQL("panel_de_los_pensamientos").query_db(query, data)
        return result

    @classmethod
    def show_thought(cls):
        query="SELECT * FROM pensamientos left JOIN users ON users.id=pensamientos.user_id;"
        results= connectToMySQL("panel_de_los_pensamientos").query_db(query)
        all_thoughts=[]
        for thoughts in results:
            thoughts_obj=cls(thoughts)
            thoughts_obj.users.append(User(thoughts))
            all_thoughts.append(thoughts_obj)
        return all_thoughts


    @classmethod
    def delete_thought(cls,data):
        query="DELETE FROM pensamientos WHERE id=%(id)s;"
        result = connectToMySQL("panel_de_los_pensamientos").query_db(query, data)
        return result

    @classmethod
    def like_thought(cls, data):
        query="INSERT INTO likes(user_id, pensamiento_id) VALUES (%(user_id)s, %(pensamiento_id)s);"
        result = connectToMySQL("panel_de_los_pensamientos").query_db(query, data)
        return result

    @classmethod
    def show_likes(cls, data):
        query="SELECT * FROM likes where pensamiento_id=%(pensamiento_id)s;"
        results = connectToMySQL("panel_de_los_pensamientos").query_db(query, data)
        likes=[]
        for like in results:
            likes.append(like)
        return len(likes)

    @classmethod
    def show_thought_user(cls,data):
        query="select * from pensamientos where user_id=%(user_id)s;"
        results = connectToMySQL("panel_de_los_pensamientos").query_db(query,data)
        thoughts =[]
        for thought in results:
            thoughts.append(cls(thought))
        return thoughts

    @staticmethod
    def validation(pensamiento):
        is_valid=True
        if len(pensamiento["content"])<5:
            flash("Pensamiento debe ser de al menos 5 caracteres", 'create_thought')
            is_valid=False
            
        return is_valid

