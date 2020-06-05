# make a prediction for a new image.
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

# load and prepare the image
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

# load an image and predict the class
def get_char(model, image_path):
    # load the image
    img = load_image(image_path)
    # load model
    # predict the class
    digit = np.argmax(model.predict(img), axis=-1)[0]
    return str(digit)

# entry point, run the example
# if __name__ == "__main__":
#     run_example()
