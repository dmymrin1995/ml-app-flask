import tensorflow as tf
from tensorflow import keras
import numpy as np


img_height = 120
img_width = 120
class_names = ['Positive', 'Negative']
img_path = './static/img/'

def get_category(img):
      path_to_file = img_path + img
      reconstructed_model = keras.models.load_model('static/model/my_h5_model (1).h5')
      img = tf.keras.utils.load_img(path_to_file, target_size=(img_height, img_width))
      img_array = tf.keras.utils.img_to_array(img)
      img_array = tf.expand_dims(img_array, 0)

      predictions = reconstructed_model.predict(img_array)
      score = tf.nn.softmax(predictions[0])

      return "This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 * np.max(score))

