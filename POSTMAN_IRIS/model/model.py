import pickle
import gzip

with gzip.open('./model/xgboost-iris.gpz', 'r') as f:
    xgboostModel = pickle.load(f)

def predict(input):
    pred = M.predict(input)[0]
    print(pred)
    return pred