import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np


model = tf.keras.models.load_model('model.h5')
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
for i in np.random.randint(0, 10000+1, 10):
    arr_img = Image.fromarray(x_train[i])
    arr_img.save('{}.png'.format(i), "PNG")