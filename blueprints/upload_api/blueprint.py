from flask import Blueprint, render_template, request, jsonify
import re
import base64
import numpy as np
import pickle
from skimage import io, color, transform
import json
from .predictor import get_char
# from .sign_predictor import get_sign
from tensorflow.keras.models import load_model
import time

def parse_image(imgData, filename='output'):
    imgData = str.encode(imgData)
    img_str = re.search(b"base64,(.*)", imgData).group(1)
    img_decode = base64.decodebytes(img_str)
    with open(filename+'.png', "wb") as f:
        f.write(img_decode)
    return img_decode

from operator import add, sub, mul, truediv
def calculate(num1, num2, sign):
    STR_TO_FUNC = {'+': add, '-': sub, '*': mul, '/': truediv}
    return str(STR_TO_FUNC[sign](int(num1), int(num2)))
 

# Load model
digit_model = load_model('models/mnist_MLM.h5')
sign_model = load_model('models/sign.h5')

upload_api = Blueprint('upload_api', __name__)

@upload_api.route('/upload/', methods=['POST'])
def upload():
    """Get drawings from request, return prediction as an string. """

    # Get images from client
    images = json.loads(str(request.get_data(), encoding='utf-8'))['images']
    filenames = ['img_left', 'img_middle', 'img_right']
    for i, img in enumerate(images):
        parse_image(img, filenames[i])

    # Start timer
    tic = time.time()

    res_middle = get_char(sign_model, 'img_middle.png')
    res_left = get_char(digit_model, 'img_left.png')
    res_right = get_char(digit_model, 'img_right.png')
    SIGN_LIST = ['/', '-', '+', '*']
    res_middle = SIGN_LIST[int(res_middle)]
    res = res_left + res_middle + res_right + ' = ' + calculate(res_left, res_right, res_middle)
    print("======> Whole result:", res, type(res))
    
    # End timer
    toc = time.time()
    print(toc-tic)

    return res
