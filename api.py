from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/pokemon/<name>', methods=['GET'])
def get_pokemon(name):
    try:
        # Solicitud a PokeAPI
        response = requests.ge(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        response.raise_for_status()
        print(response.raise_for_status())

        # Retorna la respuesta JSON de la API
        return jsonify(response.json()), 200
    except requests.exceptions.HTTPError as http_err:
        # Si el Pokémon no se encuentra, retorna un error 404
        if response.status_code == 404:
            return jsonify({"error": "Pokémon no encontrado"}), 404
        # Cualquier otro error de HTTP
        return jsonify({"error": str(http_err)}), response.status_code
    except Exception as e:
        # Error de servidor
        return jsonify({"error": "Error interno del servidor"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
