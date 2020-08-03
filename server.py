from flask import Flask, request
from flask_cors import CORS, cross_origin
import game

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

game_instances = {}


@app.route('/get_test')
def get_test():
    return 'Porca madonna de li compiuter de cristo'


@app.route('/start_game', methods=["GET"])
def start_game():
    if request.method == 'GET':
        return ''


@app.route('/coordinates', methods=["POST"])
def coordinates():
    if request.method == 'POST':
        text = request.json
    return text


if __name__ == "__main__":
    app.run(debug=True)
