from flask import Flask, request, jsonify
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

labels ={
  0: "setosa",
  1: "versicolor",
  2: "virginica"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    #output = round(prediction[0], 2)
    #output = (prediction[0])
    output =labels[prediction[0]]
    return render_template('index.html', prediction_text='IRIS prediction is'.format(output))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')