from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np

from keras.models import load_model

app = Flask(__name__)

# Load the trained model
model = load_model('leather_defect_model.h5')
defect_classes = ['Folding marks', 'Grain off', 'Growth marks', 'loose grains', 'non defective', 'pinhole']

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/output', methods=['POST','GET'])
def predict():
    # Load and preprocess the input image from the request
    input_image = request.files['image'].read()
    nparr = np.fromstring(input_image, np.uint8)
    input_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    input_image = cv2.resize(input_image, (224, 224))
    input_image = input_image.astype('float32') / 255
    input_image = np.expand_dims(input_image, axis=0)

    # Predict the defect from the input image
    predictions = model.predict(input_image)
    predicted_class_index = np.argmax(predictions)
    predicted_defect = defect_classes[predicted_class_index]
    print(predicted_defect)
    return render_template('output.html',predicted_defect=predicted_defect)  # Render the output HTML page with the predicted defect label



if __name__=="__main__":
    app.run(debug=True)
