from flask import Flask, jsonify
from current_read import CurrentRead
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_current_read():
    peepee = CurrentRead()
    return {'attrs': peepee.attrs}

@app.route('/get_current_read', methods=['GET'])
def get_current_read_route():
    result = get_current_read()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)