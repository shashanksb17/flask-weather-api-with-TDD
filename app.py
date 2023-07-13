from flask import Flask, jsonify, request


weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home_page():       
        return jsonify('welcome to tdd flask app')

    @app.route('/weather/<string:city>', methods=['GET'])
    def get_weather(city):
        if city in weather_data:
            return jsonify(weather_data[city])
        else:
            return jsonify({'error': 'City not found'}), 404

    @app.route('/weather', methods=['POST'])
    def create_weather():
        new_weather = request.get_json()
        city = new_weather.get('city')
        if city in weather_data:
            return jsonify({'error': 'Weather data already exists for this city'}), 400
        else:
            weather_data[city] = new_weather
            return jsonify(new_weather), 201

    @app.route('/weather/<string:city>', methods=['PUT'])
    def update_weather(city):
        if city in weather_data:
            updated_weather = request.get_json()
            weather_data[city].update(updated_weather)
            return jsonify(weather_data[city])
        else:
            return jsonify({'error': 'City not found'}), 404

    @app.route('/weather/<string:city>', methods=['DELETE'])
    def delete_weather(city):
        if city in weather_data:
            deleted_weather = weather_data.pop(city)
            return jsonify({'message': f'Weather data for {city} deleted'})
        else:
            return jsonify({'error': 'City not found'}), 404


    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
