from pensamientos_app import app
from pensamientos_app.controllers import users_controller, pensamientos_controller

if __name__ == "__main__":
    app.run(debug=True)