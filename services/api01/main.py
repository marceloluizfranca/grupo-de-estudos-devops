# server.py
import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

data =  {
        'title': "API 01",
        'version': "1.0.0",
        'status': "up",
        'datetime': str(datetime.datetime.now())
        }

@app.route('/', methods=['POST'])
def status():
    return jsonify(data)

@app.route('/challenge/<username>', methods=['GET'])
def get_challenge(username):
    return jsonify({'name': username})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)