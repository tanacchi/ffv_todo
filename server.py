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
    return jsonify({"status": 202})

@app.route('/api/items/create', methods=['POST'])
def create_item():
    post_data = request.get_json()
    item_id = post_data['id']
    title = post_data['title']
    newitem = {
        u'title': title,
        u'done': False
    }
    db_items.document(item_id).set(newitem)
    return jsonify({"status": 202})

@app.errorhandler(404)
def notfound_error(error):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
