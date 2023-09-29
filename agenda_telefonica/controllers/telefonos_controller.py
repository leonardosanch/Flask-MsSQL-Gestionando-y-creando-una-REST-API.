
from model.gestor_agenda import db
from model.gestor_agenda import  tb_telefonos
from flask import jsonify
def show_all_phone():
   "select *from telefonos"
   telefonos = tb_telefonos.query.all()
   data = []
   for telefono in telefonos:
       data.append({
           "id": telefono.id,
           "usuario_id": telefono.usuario_id,
           "telefono": telefono.telefono,
           "tipo": telefono.tipo

       })
   return jsonify(data)


def get_phone_id(id):
    "select *from telefonos where id = id"
    telefonos = tb_telefonos.query.filter_by(id=id).all()
    data = []
    for telefono in telefonos:
        data.append({
            "id": telefono.id,
            "usuario_id": telefono.usuario_id,
            "telefono": telefono.telefono,
            "tipo": telefono.tipo


        })

    return jsonify(data)

def store_register(new_data):
    "insert into telefonos (usuario_id, telefono, tipo) values(new_data.usuario_id, new_data.telefono, new_data.tipo)"
    try:
        usuario_id= new_data['usuario_id']
        telefono = new_data['telefono']
        tipo = new_data['tipo']
        telefono = tb_telefonos(usuario_id, telefono, tipo)
        db.session.add(telefono)
        db.session.commit()
        return "data inserted"
    except Exception as ex:
        db.session.rollback()
        return f"Error insertando datos. Se ha realizado un rollback de la data. MSG:{ex}"


def updated_data(data_to_update):
    "update telefonos set [campos a modificar ] =[valores o modificar] where id=id"
    try:
        id = data_to_update['id']
        telefono = tb_telefonos.query.filter_by(id=id).first()
        telefono.usuario_id = data_to_update['usuario_id']
        telefono.telefono = data_to_update['telefono']
        telefono.tipo = data_to_update['tipo']
        db.session.merge(telefono)
        db.session.flush()
        db.session.commit()
        return "El update se ha realizado exitosamente"
    except Exception as ex:
        db.session.rollback()
        return f"Error actualizando  datos. Se ha realizado un rollback de la data. MSG:{ex}"



def deleted_data(data_to_delete):
    id = data_to_delete['id']
    "delete from telefonos where id = id"
    telefono = tb_telefonos.query.filter_by(id=id).first()
    if telefono:
        db.session.delete(telefono)
        db.session.commit()
        return "Dato borrado"
    return "Error tratando de borrar datos"

