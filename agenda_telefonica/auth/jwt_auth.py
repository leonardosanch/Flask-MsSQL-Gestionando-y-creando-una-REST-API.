import bcrypt
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify

from model.gestor_agenda import tb_login, db

jwt_auth_bp = Blueprint('auth', __name__)

@jwt_auth_bp.route("/")
def index():
    return "index from auth"


@jwt_auth_bp.route("/", methods= ['POST'])
def create_user():
    data = request.get_json()
    usuario = data['usuario']
    clave = data['clave']
    nivel = data['nivel']
    clave_encriptada = bcrypt.hashpw(clave.encode('utf-8'),bcrypt.gensalt())
    insert_user = tb_login(usuario,clave_encriptada ,nivel)
    db.session.add(insert_user)
    db.session.commit()
    return "Usuario insertado"

@jwt_auth_bp.route("/create_token", methods= ['POST'])
def create_token():
    try:
        data = request.get_json()
        usuario = data['usuario']
        clave = data['clave']

        get_user = tb_login.query.filter_by(usuario = usuario).first()
        check_clave = bcrypt.checkpw(str(clave).encode('utf-8'),str(get_user.clave).encode('utf-8'))
        if not get_user or not check_clave:
            return jsonify({"msg":"Usuario o clave incorrecto"}),401
        acces_token = create_access_token(identity={"usuario_id":get_user.id,"nivel_usuario":get_user.nivel})
        return jsonify({"token":'Bearer'+acces_token})
    except Exception as ex:
        return  f"Error creando JWT {ex}"








