from flask import Flask, request
app = Flask(__name__)

@app.route('/hello')
def get_hello_world():
    name = request.args.get('name')
    if name == None:
        name = "world"
    return {'hello': name}

@app.route('/hello/<name>')
def get_hello_name(name):
    return {'hello': name}

@app.route('/hello', methods=['POST'])
def post_hello_name():
    data = request.get_json()
    return {'hello': data['name']}

if __name__ == "__main__":
    app.run(debug=True)