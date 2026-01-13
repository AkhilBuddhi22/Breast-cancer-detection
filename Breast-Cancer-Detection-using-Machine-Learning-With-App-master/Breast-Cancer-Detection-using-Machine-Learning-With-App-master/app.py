from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
from pathlib import Path

# loading model from repo-relative path
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'models' / 'model.pkl'
model = pickle.load(open(MODEL_PATH, 'rb'))

# flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    features = request.form['feature']
    features = features.split(',')
    np_features = np.asarray(features, dtype=np.float32)

    # prediction
    pred = model.predict(np_features.reshape(1, -1))
    message = ['Cancrouse' if pred[0] == 1 else 'Not Cancrouse']
    # print(message[0])
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)

