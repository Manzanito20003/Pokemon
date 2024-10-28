from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/pokemon/<name>', methods=['GET'])
def get_pokemon(name):
    try:
        # Solicitud a PokeAPI
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        response.raise_for_status()

        # Limpiar y extraer la información importante de la respuesta JSON
        cleaned_data = clean_response_pokemon(response.json())

        # Retorna la respuesta limpia
        return jsonify(cleaned_data), 200
    except requests.exceptions.HTTPError as http_err:
        # Si el Pokémon no se encuentra, retorna un error 404
        if response.status_code == 404:
            return jsonify({"error": "Pokémon no encontrado"}), 404
        # Cualquier otro error de HTTP
        return jsonify({"error": str(http_err)}), response.status_code
    except Exception as e:
        # Error de servidor
        return jsonify({"error": "Error interno del servidor"}), 500


def clean_response_pokemon(json):
    # Extraer habilidades
    abilities = [
        {
            "name": ability["ability"]["name"],
            "is_hidden": ability["is_hidden"]
        }
        for ability in json.get("abilities", [])
    ]

    # Extraer otros detalles
    name = json.get("forms", [{}])[0].get("name")
    pokemon_id = json.get("id")
    base_experience = json.get("base_experience")
    type_ = json.get("types", [{}])[0].get("type", {}).get("name")
    weight = json.get("weight")


    # Construir la respuesta limpia
    cleaned_data = {
        "name": name,
        "id": pokemon_id,
        "type": type_,
        "weight": weight,
        "abilities": abilities,
        "base_experience": base_experience,

    }

    return cleaned_data


if __name__ == '__main__':
    app.run(debug=True, port=5000)
