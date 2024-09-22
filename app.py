import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    # Set prediction_text to None initially
    return render_template('index.html', prediction_text=None)


@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs
    float_features = [float(x) for x in request.form.values()]
    f = [np.array(float_features)]

    # Predict water potability
    prediction = model.predict(f)
    if prediction == 0:
        result = "Given Water sample is not Potable"
    else:
        result = "Given Water sample is Potable"

    # Render the result in the template
    return render_template('index.html', prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)
