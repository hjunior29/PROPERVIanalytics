from services.data_fetcher import *
from flask import jsonify
from datetime import datetime
import requests

def configure_routes(app):

    @app.route('/', methods=['GET'])
    def status():
        message = "Microservice for data analytics and AI!"
        status = "running"
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return jsonify({
            "message": message,
            "status":  status,
            "time":    currentTime,
        })

    @app.route('/collect-data', methods=['GET'])
    def collect_data():
        try:
            
            url = "http://localhost:8080/get-properties"
            response = requests.get(url)
            response.raise_for_status()
            
            if response.status_code != 200:
                return jsonify({"error": "Failed to fetch data from Go microservice"}), 500

            data = response.json()
            return jsonify(data)

        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return jsonify(data)

    @app.route('/average-price', methods=['GET'])
    def data_fetcher():
        avg_price = get_average_price()
        return jsonify({
            "average_price": avg_price
        })
