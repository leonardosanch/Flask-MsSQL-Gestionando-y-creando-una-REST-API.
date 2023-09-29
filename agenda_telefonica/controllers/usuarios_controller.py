
from model.gestor_agenda import db
from model.gestor_agenda import  tb_usuarios
from flask import jsonify
def show_all_users():
    usuarios = tb_usuarios.query.all()
    data = []
    for usuario in usuarios:
        data.append({
            "id":usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "apodo": usuario.apodo


       })
    return  jsonify(data)


def get_user_id(id):
    "select *from usuarios where id=id"
    usuarios = tb_usuarios.query.filter_by(id=id).all()
    data = []
    for usuario in usuarios:
        data.append({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "apodo": usuario.apodo

        })

    return jsonify(data)


def store_register(new_data):
    "insert into usuarios (nombre, apellido,apodo) values(new_data.nombre, new_data.apellido, new_data.apodo)"
    nombre = new_data['nombre']
    apellido = new_data['apellido']
    apodo = new_data['apodo']
    usuario = tb_usuarios(nombre,apellido,apodo)
    db.session.add(usuario)
    db.session.commit()
    return "data inserted"


def updated_data(data_to_update):
    "update usuarios set [campos a modificar ] =[valores o modificar] where id=id"
    id = data_to_update['id']
    usuario = tb_usuarios.query.filter_by(id=id).first()
    usuario.nombre = data_to_update['nombre']
    usuario.apellido = data_to_update['apellido']
    usuario.apodo = data_to_update['apodo']
    db.session.merge(usuario)
    db.session.flush()
    db.session.commit()
    return "El update se ha realizado exitosamente"

def deleted_data(data_to_delete):
    id = data_to_delete['id']
    "delete from usuarios where id = id"
    usuario = tb_usuarios.query.filter_by(id=id).first()
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return "Dato borrado"
    return "Error tratando de borrar datos"






