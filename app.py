from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configuration de la connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['DBLP']
publis_collection = db['publis']

# Route de base
@app.route('/')
def index():
    return "Welcome to the DBLP Publis API!"

@app.route('/publis', methods=['GET'])
def get_publis():
    publis = []
    for publi in publis_collection.find():
        publis.append({
            'title': publi['title'],
            'authors': publi['authors']
        })
    return jsonify(publis)

@app.route('/publi/<title>', methods=['GET'])
def get_publi(title):
    publi = publis_collection.find_one({'title': title})
    if publi:
        return jsonify({
            'title': publi['title'],
            'authors': publi['authors']
        })
    return jsonify({'error': 'Publication not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
