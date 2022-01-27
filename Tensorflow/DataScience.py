# Import constant from TensorFlow
from tensorflow import constant
import tensorflow
from tensorflow import Variable
import matplotlib.pyplot as plt
# example of converting an image with the Keras API
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
import numpy as np
import glob

# https://stackoverflow.com/questions/4601373/better-way-to-shuffle-two-numpy-arrays-in-unison
def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]


def imageToArray(path):
    img = load_img(path, color_mode="grayscale")
    img_array = img_to_array(img)
    img_np = np.array([img_array])
    img_np = img_np.reshape(45, 45)
    img_np /= 255.0
    return img_np


ffilelist = glob.glob('Letters/f30/*.jpg')
lfilelist = glob.glob('Letters/l30/*.jpg')

fArray = np.array([imageToArray(fname) for fname in ffilelist])
lArray = np.array([imageToArray(fname) for fname in lfilelist])
letterArray = np.concatenate((fArray, lArray))
print(letterArray.shape)
labelArray = np.append(np.zeros((30, 1)), np.ones((30, 1)))
letterArray_shuffled, labelArray_shuffled = unison_shuffled_copies(letterArray, labelArray)


print(labelArray_shuffled[0])
plt.imshow(letterArray_shuffled[0], interpolation='nearest')
plt.show()

print(labelArray_shuffled[3])
plt.imshow(letterArray_shuffled[3], interpolation='nearest')
plt.show()

print(labelArray_shuffled[20])
plt.imshow(letterArray_shuffled[20], interpolation='nearest')
plt.show()