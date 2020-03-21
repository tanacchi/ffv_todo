from flask import (
    Flask, render_template, send_from_directory,
    jsonify,
)
from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


app = Flask(__name__,
            template_folder='./dist',
            static_folder='./dist')
CORS(app)

cred = credentials.Certificate('ffv-todo-app-firebase-adminsdk-4sdgu-9157c7cf91.json')
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()
db_items = db.collection(u'items')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<path:path>')
def file(path):
    return send_from_directory('./dist', path)

@app.route('/api/items')
def todo_items():
    #  items = db_items.stream()
    items = [
        { 'id': 1, 'title': "Todo Item 1", 'done': False },
        { 'id': 2, 'title': "Todo Item 2", 'done': True  }
    ]
    return jsonify(items)


if __name__ == '__main__':
    app.run(debug=True)
