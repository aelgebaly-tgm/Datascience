# Import constant from TensorFlow
from tensorflow import constant
import tensorflow
from tensorflow import Variable
import matplotlib.pyplot as plt
# example of converting an image with the Keras API
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from tensorflow import keras
import numpy as np
import glob


# Show a visualization of an array
def arrayToImage(array):
    plt.imshow(array, interpolation='nearest')
    plt.show()

# https://stackoverflow.com/questions/4601373/better-way-to-shuffle-two-numpy-arrays-in-unison
def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]


# Take an image and return an array
def imageToArray(path):
    img = load_img(path, color_mode="grayscale")
    img_array = img_to_array(img)
    img_np = np.array([img_array])
    img_np = img_np.reshape(45, 45)
    img_np /= 255.0
    return img_np
	
	
################Initialize################             

#Filelists
ffilelist = glob.glob('Letters/f30/*.jpg')
lfilelist = glob.glob('Letters/l30/*.jpg')

#create Arrays out of the images (and shuffle them)
fArray = np.array([imageToArray(fname) for fname in ffilelist])
np.random.shuffle(fArray)
lArray = np.array([imageToArray(fname) for fname in lfilelist])
np.random.shuffle(lArray)

#split the arrays into 20-10 Arrays
fTraining, fTest = np.split(fArray, [20,])
lTraining, lTest = np.split(lArray, [20,])

#add the different letters together into training and label arrays
letterTraining = np.concatenate((fTraining, lTraining))
letterTest = np.concatenate((fTest, lTest))


# Add a label array (0 = letter 0, 1 = letter 1)
labelTraining = np.append(np.zeros((20, 1)), np.ones((20, 1)))
labelTest = np.append(np.zeros((10, 1)), np.ones((10, 1)))

# Shuffel the label and training arrays at the same time, so that ex Letter 2 still corresponds to its original label
letterTraining_shuffled, labelTraining_shuffled = unison_shuffled_copies(letterTraining, labelTraining)

################Initialize################  



################Model 1################  
model_1 = keras.Sequential()
model_1.add(keras.layers.Dense(8, activation='softmax', input_shape=(45,45,)))
model_1.add(keras.layers.Dense(8, activation='softmax'))
model_1.add(keras.layers.Dense(1, activation='sigmoid'))
model_1.compile(optimizer=keras.optimizers.Adam(lr=0.001), loss='binary_crossentropy')
model_1.fit(fTraining, np.zeros((20,1)), epochs=1000, validation_split=0.5)
model_1.fit(lTraining, np.ones((20,1)), epochs=1000, validation_split=0.5)
################Model 1################  


################Model 2################  
model_2 = keras.Sequential()
model_2.add(keras.layers.Dense(8, activation='softmax', input_shape=(45,45,)))
model_2.add(keras.layers.Dense(8, activation='softmax'))
model_2.add(keras.layers.Dense(1, activation='sigmoid'))
model_2.compile(optimizer=keras.optimizers.Adam(lr=0.001), loss='binary_crossentropy')
model_2.fit(letterTraining_shuffled, labelTraining_shuffled, epochs=2000, validation_split=0.5)
################Model 2################ 

 
################Model 3################  
model_3 = keras.Sequential()
model_3.add(keras.layers.Dense(4, activation='softmax', input_shape=(45,45,)))
model_3.add(keras.layers.Dense(4, activation='softmax'))
model_3.add(keras.layers.Dense(4, activation='softmax'))
model_3.add(keras.layers.Dense(4, activation='softmax'))
model_3.add(keras.layers.Dense(4, activation='softmax'))
model_3.add(keras.layers.Dense(1, activation='sigmoid'))
model_3.compile(optimizer=keras.optimizers.Adam(lr=0.001), loss='binary_crossentropy')
model_3.fit(letterTraining_shuffled, labelTraining_shuffled, epochs=2000, validation_split=0.5)
################Model 3################  


################Model 4################  
model_4 = keras.Sequential()
model_4.add(keras.layers.Dense(16, activation='relu', input_shape=(45,45,)))
model_4.add(keras.layers.Dense(1, activation='sigmoid'))
model_4.compile(optimizer=keras.optimizers.Adam(lr=0.001), loss='binary_crossentropy')
model_4.fit(letterTraining_shuffled, labelTraining_shuffled, epochs=2000, validation_split=0.5)
################Model 4################  

################Model 5################  
model_5 = keras.Sequential()
model_5.add(keras.layers.Dense(16, activation='softmax', input_shape=(45,45,)))
model_5.add(keras.layers.Dense(1, activation='sigmoid'))
model_5.compile(optimizer=keras.optimizers.Adam(lr=0.001), loss='binary_crossentropy')
model_5.fit(letterTraining_shuffled, labelTraining_shuffled, epochs=2000, validation_split=0.5)
################Model 4################  



print("MODEL 1 EVALUATION, first F then L")
print(model_1.evaluate(letterTest, labelTest))
print("MODEL 2 EVALUATION, 2 softmax Layers")
print(model_2.evaluate(letterTest, labelTest))
print("MODEL 3 EVALUATION, 5 softmax Layers")
print(model_3.evaluate(letterTest, labelTest))
print("MODEL 4 EVALUATION, 1 relu layer")
print(model_4.evaluate(letterTest, labelTest))
print("MODEL 5 EVALUATION, 1 softmax Layer")
print(model_5.evaluate(letterTest, labelTest))
















