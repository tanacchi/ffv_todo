import os

from flask import (
    Flask, render_template, send_from_directory,
    jsonify, request, redirect
)
from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


app = Flask(__name__,
            template_folder='./dist',
            static_folder='./dist')
CORS(app)

FIREBASE_CONFIG_PROPERTIES = (
    'FIREBASE_AUTH_TYPE', 'FIREBASE_AUTH_PROJECT_ID', 'FIREBASE_AUTH_PRIVATE_KEY_ID',
    'FIREBASE_AUTH_PRIVATE_KEY', 'FIREBASE_AUTH_CLIENT_EMAIL', 'FIREBASE_AUTH_CLIENT_ID',
    'FIREBASE_AUTH_AUTH_URI', 'FIREBASE_AUTH_TOKEN_URI', 'FIREBASE_AUTH_AUTH_PROVIDER_X509_CERT_URL',
    'FIREBASE_AUTH_CLIENT_X509_CERT_URL',
)
FIREBASE_CONFIG = {
    cfg_property[len('FIREBASE_AUTH_'):].lower() : os.environ[cfg_property] for cfg_property in FIREBASE_CONFIG_PROPERTIES
}

cred = credentials.Certificate(FIREBASE_CONFIG)
firebase = firebase_admin.initialize_app(cred)
del FIREBASE_CONFIG_PROPERTIES, FIREBASE_CONFIG

db = firestore.client()
db_items = db.collection(u'items')
db_lists = db.collection(u'lists')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<path:path>')
def file(path):
    return send_from_directory('./dist', path)

@app.route('/api/items', methods=['POST'])
def update_item():
    post_data = request.get_json()
    list_id = post_data['list_id']
    item_id = post_data['item_id']

    target_item = db_lists.document(list_id).collection(u'items').document(item_id)
    done = {"true": True, "false": False}[post_data['done']]
    target_item.update({u'done': done})
    return jsonify({"status": 202})

@app.route('/api/items/create', methods=['POST'])
def create_item():
    post_data = request.get_json()
    list_id = post_data['list_id']
    title = post_data['title']
    newitem = {
        u'title': title,
        u'done': False
    }
    target_list = db_lists.document(list_id).collection(u'items').document().set(newitem)
    return jsonify({"status": 202})

@app.route('/api/lists')
def todo_lists():
    docs = db_lists.stream()
    lists = { doc.id: {'name': doc.to_dict()['name']} for doc in docs }
    return jsonify(lists)

@app.route('/api/lists/create', methods=['POST'])
def create_list():
    post_data = request.get_json()
    name = post_data['name']
    newlist = {
        u'name': name,
    }
    db_lists.document().set(newlist)
    return jsonify({"status": 202})

@app.route('/api/lists/<string:list_id>')
def list_show(list_id):
    target_list = db_lists.document(list_id).get().to_dict()
    items = db_lists.document(list_id).collection(u'items').stream()
    items = { doc.id: doc.to_dict() for doc in items }
    target_list.update({'items': items})
    return jsonify(target_list)

@app.errorhandler(404)
def notfound_error(error):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
