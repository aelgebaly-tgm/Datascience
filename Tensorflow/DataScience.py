# Import constant from TensorFlow
from tensorflow import constant
import tensorflow
from tensorflow import Variable
import matplotlib.pyplot as plt
# example of converting an image with the Keras API
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from sklearn.utils import shuffle
import numpy as np
import glob



def imageToArray(path):
    img = load_img(path, color_mode = "grayscale")
    print(img)
    img_array = img_to_array(img)
    img_np = np.array([img_array])
    img_np = img_np.reshape(45,45)
    img_np /= 255.0
    return img_np

ffilelist = glob.glob('Letters/f30/*.jpg')
lfilelist = glob.glob('Letters/l30/*.jpg')

fArray= np.array([imageToArray(fname) for fname in ffilelist])
lArray= np.array([imageToArray(fname) for fname in lfilelist])
letterArray = np.concatenate((fArray,lArray))
print(letterArray.shape)
labelArray = np.append(np.zeros((1, 30))[0] , np.ones((1,30))[0])

array1_shuffled, array2_shuffled = sklearn.utils.shuffle(array1, array2)


