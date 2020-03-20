from flask import (
    Flask, render_template, send_from_directory,
    jsonify,
)
from flask_cors import CORS

app = Flask(__name__,
            template_folder='./dist',
            static_folder='./dist')
CORS(app)

#  @app.route('/<path:path>')
#  @app.route('/', defaults={'path': ''})
#  def root(path):
    #  print("path", path)
    #  return render_template('index.html')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<path:path>')
def file(path):
    return send_from_directory('./dist', path)

@app.route('/api/items')
def todo_items():
    items = [
        { 'id': 1, 'title': "Todo Item 1", 'done': False },
        { 'id': 2, 'title': "Todo Item 2", 'done': True  }
    ]
    return jsonify(items)

app.run(debug=True)
