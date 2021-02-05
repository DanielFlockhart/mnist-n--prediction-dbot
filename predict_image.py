import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL.ImageOps  
import os
def convert_image(name):
    img = Image.open(name)
    img = img.resize((28, 28))
    img = img.convert('L')
    img = PIL.ImageOps.invert(img)
    img = np.asarray(img)
    img = tf.keras.utils.normalize([img], axis=1)
    return img

def get_pred():
    nme = 'num.png'
    image = convert_image(nme)
    model = tf.keras.models.load_model("mnist_numbers.model")
    predictions = model.predict([image])
    with open("res.txt", "w+") as f:
        f.write(str(np.argmax(predictions[0])))

if __name__ == "__main__":
    get_pred()
