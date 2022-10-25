from recetas_app.controller import recetas_controlador, usuarios_controlador
from recetas_app import app
app.secret_key="chocolate"
if __name__=="__main__":
    app.run(debug=True)