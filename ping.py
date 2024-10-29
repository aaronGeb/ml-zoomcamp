
from flask import Flask, request, jsonify
app = Flask('ping')

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong\n'


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=9696)