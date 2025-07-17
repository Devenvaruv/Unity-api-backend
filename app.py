import os
from flask import Flask, request, jsonify

app = Flask(__name__)

stored_data = []  # optional, in-memory store for receiver testing

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print("Received at /submit:", data)

    # Forward to /receiver
    response = app.test_client().post('/receiver', json=data)

    if response.status_code != 200:
        return jsonify({'status': 'error', 'details': response.get_data(as_text=True)}), 500

    return jsonify({'status': 'ok'}), 200

@app.route('/receiver', methods=['POST'])
def receiver():
    data = request.json
    print("Received at /receiver:", data)
    stored_data.append(data)
    return jsonify({'received': True}), 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(stored_data), 200

@app.route('/')
def home():
    return 'Backend is running', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
