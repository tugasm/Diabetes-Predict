from flask import Flask, render_template, request,  jsonify
import requests
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input = request.form
        x = np.array([[input['pg'], input['gl'], input['bp'], input['st'],
                       input['ins'], input['bmi'], input['dpf'], input['age']]])
        prediksi = model.predict_proba(x)[:, 1]
        data = round(prediksi[0]*100)

        # print('mas

        # model = joblib.load('model_diabetes')
        return render_template('hasil.html', data=data)


if __name__ == '__main__':
    model = joblib.load('model_diabetes')
    app.run(debug=True)
