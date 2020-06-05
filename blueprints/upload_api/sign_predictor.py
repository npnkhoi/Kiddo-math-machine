import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

# def preprocess(path):
#     """ Take the path, return the preprocessed image """
#     image = tf.io.read_file(path)
#     image = tf.image.decode_jpeg(image, channels=3)
#     image = tf.image.rgb_to_grayscale(image)
#     image = tf.image.resize(image, [45, 45])
#     image = tf.image.convert_image_dtype(image, dtype=tf.float32)
#     # image = tf.squeeze(image, axis=-1)
#     image = 255 - image  # revert black-white
#     # image = image.astype('float32')
#     image /= 255.0  # normalize to [0,1] range
#     # image = 2*image-1  # normalize to [-1,1] range
#     # print("Image shape:", image.shape)
#     image = image.reshape(1, 45, 45, 1)
#     return image


def load_image(filename):
    # load the image
    img = load_img(filename, color_mode='grayscale', target_size=(28, 28))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 1 channel
    img = img.reshape(1, 28, 28, 1)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    img = 1 - img
    return img

def get_char(model, image_path):
    LABEL_TO_INDEX = {0: '/', 1: '-', 2: '+', 3: '*'}
    # model = tf.keras.models.load_model(model_path)
    # input_data = np.array([preprocess(image_path)])
    # prediction = np.argmax(model.predict(load_image(image_path)), axis=-1)[0]
    img = load_image(image_path)
    prediction = np.argmax(model.predict(img), axis=-1)[0]
    return LABEL_TO_INDEX[prediction]

