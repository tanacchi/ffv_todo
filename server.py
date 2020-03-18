from flask import Flask, render_template, send_from_directory

app = Flask(__name__,
            template_folder='./view/dist',
            static_folder='./view/dist')

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
    return send_from_directory('./view/dist', path)


app.run(debug=True)
