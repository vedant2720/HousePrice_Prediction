# app.py
from flask import Flask, request, jsonify
import mlflow.sklearn
import numpy as np

app = Flask(__name__)
model = mlflow.sklearn.load_model("model_dir") # Load from directory

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    return jsonify({'prediction': model.predict(features).tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)