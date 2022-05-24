import numpy as np
import model


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello'

@app.route('/predict', method=['POST'])
def postInput():
    inval = request.get_json()
    x1 = inval['a']
    x2 = inval['b']
    x3 = inval['c']
    x4 = inval['d']
    input = np.array([[x1,x2,x3,x4]])
    print(input)
    return jsonify({'return': 'ok'})
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000, debug = True)