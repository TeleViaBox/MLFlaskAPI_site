# MLFlaskAPI_site


## 1. Python Flask API
### Structure:
```
.
├── model
│   └── xgboost-iris.pgz
├── model.py
├── requirements.txt
└── run.py
```
### Route:
- ./test
- ./predict

```python
@app.route('/test', methods=['GET'])
def getResult():
    input = np.array([[num1, num2, num3, num4]])
    result = model.predict(input)
    return jsonify({'result': str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    # get from FRONTEND
    insertValues = request.get_json()
    ...
    input = np.array([[x1, x2, x3, x4]])

    # PREDICT:
    result = model.predict(input)

    return jsonify({'result': str(result)})
```

## 2. Deploy Flask API on Heroku
Procfile: a setting file for HEROKU

