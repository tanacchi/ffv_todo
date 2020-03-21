from flask import (
    Flask, render_template, send_from_directory,
    jsonify, request
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
    docs = db_items.stream()
    items = { doc.id: doc.to_dict() for doc in docs }
    return jsonify(items)

@app.route('/api/items/<string:item_id>')
def update_item(item_id):
    target_item = db_items.document(item_id)
    done = {"true": True, "false": False}[request.args.get('done')]
    target_item.update({u'done': done})
    return jsonify({})

@app.route('/api/items/create', methods=['POST'])
def create_item():
    post_data = request.get_data()
    item_id = post_data['id']
    newitem = {
        u'title': post_data['title'],
        u'done': False
    }
    db_items.document(item_id).set(newitem)


if __name__ == '__main__':
    app.run(debug=True)
