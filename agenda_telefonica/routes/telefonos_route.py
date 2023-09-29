from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from controllers.telefonos_controller import show_all_phone, get_phone_id, store_register,updated_data, deleted_data
from validations.telefonos_validation import validate_data

telefonos_bp = Blueprint('telefonos', __name__)


#metodo get
@telefonos_bp.route("/")
def index():
    return show_all_phone()



@telefonos_bp.route("/<int:id>")
def get_user_by_id(id):
    return get_phone_id(id)


@telefonos_bp.route("/", methods=['POST'])
@jwt_required()
def store_data():
    new_data = request.get_json()
    response_from_validation = validate_data(new_data)
    is_valid =response_from_validation[0]
    error = response_from_validation[1]
    if is_valid:
        return store_register(new_data)
    return error, 422


@telefonos_bp.route("/", methods=['PUT'])
def update_data():
    data_to_update = request.get_json()
    response_from_validation = validate_data(data_to_update)
    is_valid = response_from_validation[0]
    error = response_from_validation[1]
    if is_valid:
         return updated_data(data_to_update)
    return error



@telefonos_bp.route("/", methods=['DELETE'])
@jwt_required()
def delete_data():
    usuario_actual = get_jwt_identity()
    usuario_actual_nivel = usuario_actual.get('nivel_usuario')
    if usuario_actual_nivel !=1:
        return "Usted no tiene permisos para borrar usuarios",401
    data_to_delete = request.get_json()
    return deleted_data(data_to_delete)