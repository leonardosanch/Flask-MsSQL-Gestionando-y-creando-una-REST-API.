def validate_data(new_data):
    usuario_id = new_data['usuario_id']
    telefono = new_data['telefono']
    tipo = new_data['tipo']
    error =[]
    response = True

    if not telefono.isdigit() or len(telefono) < 3:
        error.append({
            "entidad": "telefono",
            "error": "la longitud debe ser mayor de 3 y solo acepta numeros"
        })
        response = False

    return response, error




