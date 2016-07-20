from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils

from model import *

(X_train, y_train), (X_test, y_test) = mnist.load_data()


X_train = X_train.reshape(60000, 1, 28, 28)
X_test = X_test.reshape(10000, 1, 28, 28)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255


Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)



# comment this to start the training from scratch
model.load_weights(filepath)



datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=False,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=False)

datagen.fit(X_train)

# fits the model on batches with real-time data augmentation:
model.fit_generator(datagen.flow(X_train, Y_train, batch_size=128),
                    samples_per_epoch=len(X_train), nb_epoch=2)


model.save_weights(filepath)
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=128)
print loss_and_metrics
