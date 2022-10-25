from burgers_app.controllers import burger_controller, users_controller
from burgers_app import app
app.secret_key = "chocolate"
if __name__=="__main__":
    app.run(debug=True)