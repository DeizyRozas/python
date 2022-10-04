from flask import Flask, render_template, redirect, request
# importar la clase de friend.py
from friend import Amigo
app = Flask(__name__)

@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    amigos = Amigo.get_all()
    return render_template("index.html", amigos=amigos)

@app.route("/crear_amigo", methods=["POST"])
def crear_amigo():
    data={
        "vnombre": request.form["vnombre"],
        "vapellido": request.form["vapellido"],
        "vocc": request.form["vocc"]
    }
    Amigo.insertar_amigo(data)
    return redirect ("/")
            
if __name__ == "__main__":
    app.run(debug=True)

