from flask import Flask
from flask_migrate import Migrate

from auth.jwt_auth import jwt_auth_bp
from model.gestor_agenda import db
from routes.telefonos_route import telefonos_bp
from routes.usuarios_route import usuarios_bp
from flask_jwt_extended import JWTManager

from flasgger import Swagger

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
db.app = app
migrate = Migrate(app, db)
jwt = JWTManager(app)

swagger = Swagger(app)

app.register_blueprint(usuarios_bp, url_prefix = "/api/usuarios")

app.register_blueprint(telefonos_bp, url_prefix = "/api/telefonos")

app.register_blueprint(jwt_auth_bp, url_prefix = "/api/auth")

if __name__ == '__main__':
    app.run()

