from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def get_hello_world():
    name = request.args.get('name', 'world')
    return {'hello': name}

@app.route('/hello/<name>')
def get_hello_name(name):
    return {'hello': name}

@app.route('/hello', methods=['POST'])
def post_hello_name():
    data = request.get_json()
    return {'hello': data.get('name', 'world')}

if __name__ == "__main__":
    app.run(debug=True)