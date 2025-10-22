from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

# Testing - EMQX RULE → Endpoint POST 
@app.route('/test', methods=['POST'])
def emqx_receiver():
    # Obtener los datos JSON enviados por EMQX 
    data = request.get_json(force=True)
    
    # Mostrar en consola para depurar
    print("Mensaje recibido desde EMQX:")
    print(data)

    # Podés procesar los datos acá si querés (guardar en DB, etc.)
    
    # Responder con éxito
    return jsonify({"status": "ok", "message": "Data received"}), 200


if __name__ == '__main__':
    # Ejecuta en el puerto 5000 por defecto
    app.run()

