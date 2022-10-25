from muro_privado_app import app
from muro_privado_app.controllers import users_controller, messages_controller


if __name__=="__main__":
    app.run(debug=True)