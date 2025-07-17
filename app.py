import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print("Received JSON:", data)
    return jsonify({'status': 'ok'}), 200

@app.route('/')
def home():
    return 'Backend is running', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
