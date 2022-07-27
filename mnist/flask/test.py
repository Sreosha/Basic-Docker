from requests import request
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
from flasgger import Swagger
from flask import Flask, request

app = Flask(__name__)
swagger = Swagger(app)


model = tf.keras.models.load_model('model.h5')

@app.route('/predict_digit', methods = ['POST'])
def predict_digit():
    """Example endpoint returning a prediction of mnist
    ---
   
    parameters:
      - name: image
        required: true
        in: formData
        type: file
    responses: 
        200:
            description: Number
    """
    img = Image.open(request.files['image'])
    img_arr = np.array(img).reshape((-1,28,28,1))
    return str(np.argmax(model.predict(img_arr)))

if __name__ == '__main__':
    app.run()