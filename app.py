import pickle
import numpy as np
from flask import Flask, request, render_template
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    f = [np.array(float_features)]
    prediction = model.predict(f)
    if prediction == 0:
        return render_template('index.html', prediction_text="Given Water sample is not Potable")
    else:
        return render_template('index.html', prediction_text="Given Water sample is Potable")


if __name__ == "__main__":
    app.run(debug=True)
