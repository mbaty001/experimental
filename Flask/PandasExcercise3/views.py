from main import app
from flask import jsonify

data = app.config.get('DATA')

@app.route("/cities")
@app.route("/cities/<city_name>")
def cities(city_name=None):
    ''' Retieves the cities data'''

    if city_name:
        city_data = data[data['cities'] == city_name]
        if len(city_data):
            return city_data.to_json(), 200
        else:
            return jsonify({'city': None}), 404
    else:
        cities = data.get('cities')
        return cities.to_json(), 200

@app.route("/citizens")
@app.route("/citizens/<city_name>")
def citizens(city_name=None):
    ''' Retieves the citizens data'''

    if city_name:
        city_data = data[data['cities'] == city_name ]
        if len(city_data):
            return jsonify({city_name: city_data.get('citizens').to_json()}), 200
        else:
            return jsonify({'city': None}), 404
    else:
        citizens = data.get('citizens')
        return citizens.to_json(), 200