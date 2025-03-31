from flask import Flask
app = Flask(__name__)

@app.route('/vault/balance', methods=['GET'])
def get_balance():
    return jsonify(offline_db.query(Balance))
