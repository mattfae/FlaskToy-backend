from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mongoClient = MongoClient('mongodb://127.0.0.1:27017')
db = mongoClient.get_database('names_db')
names_col = db.get_collection('names_col')

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

@app.route('/movies')
def returnMovies():
    return jsonify(movies)


if __name__ == "__main__":
    app.run(debug=True)
