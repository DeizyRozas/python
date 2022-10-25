from dojos_y_ninjas_app.controllers import dojos_controller, ninjas_controller
from dojos_y_ninjas_app import app
app.secret_key = "chocolate"
if __name__=="__main__":
    app.run(debug=True)