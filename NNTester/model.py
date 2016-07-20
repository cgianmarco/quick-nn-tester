from keras.models import Sequential
from keras.layers import Convolution2D, Activation, MaxPooling2D, Dropout, Flatten, Dense
from keras.optimizers import SGD


default_model = Sequential()

default_model.add(Convolution2D(32, 3, 3, border_mode='valid', input_shape=(1, 28, 28)))
default_model.add(Activation('relu'))
default_model.add(Convolution2D(32, 3, 3))
default_model.add(Activation('relu'))
default_model.add(MaxPooling2D(pool_size=(2, 2)))
default_model.add(Dropout(0.25))

default_model.add(Convolution2D(64, 3, 3, border_mode='valid'))
default_model.add(Activation('relu'))
default_model.add(Convolution2D(64, 3, 3))
default_model.add(Activation('relu'))
default_model.add(MaxPooling2D(pool_size=(2, 2)))
default_model.add(Dropout(0.25))

default_model.add(Flatten())
default_model.add(Dense(256))
default_model.add(Activation('relu'))
default_model.add(Dropout(0.5))

default_model.add(Dense(10))
default_model.add(Activation('softmax'))

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
default_model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])