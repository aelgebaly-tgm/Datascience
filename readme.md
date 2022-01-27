# Data Science ``Neuronale Netzwerke - TensorFlow''

Lilly Elgebaly und Jonas Trebicki 5CHIT

2021-01-27

----

Nutze deine erworbenen Fertigkeiten zum Erstellen von TensorFlow  Modellen, um für den Datensatz zur Bilderkennung ein Neuronales Netzwerk anzupassen.

Nutze dafür einen [Datensatz zur Mustererkennung von handgeschriebenen Mathematiksymbolen](https://www.kaggle.com/xainano/handwrittenmathsymbols) von  [kaggle](https://www.kaggle.com/).

----

Es wird mit Python umgesetzt

### Daten/Bilder einlesen

Zuerst wird mithilfe des glob packages in python alle Bilder eingelesen

```
ffilelist = glob.glob('Letters/f30/*.jpg')
lfilelist = glob.glob('Letters/l30/*.jpg')
```

Danach wird ein Numpy Array geschaffen, welches aus 2D Arrays der Bilder besteht (siehe nächste Methode *imageToArray*)

```
fArray = np.array([imageToArray(fname) for fname in ffilelist])
lArray = np.array([imageToArray(fname) for fname in lfilelist])
```

imageToArray lädt die einzelnen Bilder in Graustufen; danach werden diese Bilder mit der Keras Methode "img_to_array" in ein tatsächliche Array umgewandelt (Keras ist eine Deep Learning API; in TensorFlow enthalten). Dieses Array ist "praktisch" dreidimensional, enthält die Pixel des Bildes und das es in Graustufen ist.

Dieses Array wird dann in ein Numpy Array gegeben; Danach wird noch Reshape verwendet, damit es ein 2D Array mit der Größe 45x45 ist. (Die gegebenen Bilder sind 45x45 Pixel). Danach wird noch jeder Wert in dem Array/der Matrix durch 255 gerechnet, damit die Werte nicht mehr von 0 bis 255 reichen, sondern nur von 0 bis 1.

```
def imageToArray(path):
    img = load_img(path, color_mode="grayscale")
    img_array = img_to_array(img)
    img_np = np.array([img_array])
    img_np = img_np.reshape(45, 45)
    img_np /= 255.0
    return img_np
```

