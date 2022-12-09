import sklearn
import tensorflow as tf
import joblib
from keras.models import load_model
from flask import Flask, render_template, request

app = Flask(__name__)

model = tf.keras.models.load_model('model.h5')
scaler = joblib.load('scaler_final.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST","GET"])
def predict():
    onehour = int(request.form['onehour'])
    twohour = int(request.form['twohour'])
    threehour = int(request.form['threehour'])
    
    data = [[onehour],[twohour],[threehour]]
    data = scaler.transform(data)
    data = data.reshape(1,3,1)
    pred = model.predict(data)
    pred = scaler.inverse_transform(pred)
    prediction_result = pred

    return render_template('index.html', prediction_result=pred)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)