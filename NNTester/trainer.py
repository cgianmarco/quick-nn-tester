from keras.callbacks import ModelCheckpoint
from keras.datasets import mnist
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator
import os

from model import *


class Trainer():

	def __init__(self, model=default_model):
		(X_train, y_train), (X_test, y_test) = mnist.load_data()


		X_train = X_train.reshape(60000, 1, 28, 28)
		X_test = X_test.reshape(10000, 1, 28, 28)
		X_train = X_train.astype('float32')
		X_test = X_test.astype('float32')
		X_train /= 255
		X_test /= 255


		Y_train = np_utils.to_categorical(y_train, 10)
		Y_test = np_utils.to_categorical(y_test, 10)

		self.X_train = X_train
		self.Y_train = Y_train

		self.X_test = X_test
		self.Y_test = Y_test

		self.model = model
		

	def train(self):

		# path to store the training checkpoint
		this_dir, this_filename = os.path.split(__file__)
		filepath = os.path.join(os.path.dirname(this_dir), 'data', 'weights.best.conv.hdf5')

		# comment this to start the training from scratch
		self.model.load_weights(filepath)

		checkpoint = ModelCheckpoint(filepath, monitor='acc', verbose=1, save_best_only=True, mode='max')
		callbacks_list = [checkpoint]

		self.model.fit(self.X_train, self.Y_train,
          callbacks=callbacks_list,
          batch_size=128, nb_epoch=1,
          verbose=1,
          validation_data=(self.X_test, self.Y_test))

		loss_and_metrics = self.model.evaluate(self.X_test, self.Y_test, batch_size=128)
		print loss_and_metrics

	def train_augmented(self):

		# path to store the training checkpoint
		this_dir, this_filename = os.path.split(__file__)
		filepath = os.path.join(os.path.dirname(this_dir), 'data', 'weights.best.conv2.hdf5')

		# comment this to start the training from scratch
		self.model.load_weights(filepath)

		datagen = ImageDataGenerator(
    	featurewise_center=True,
    	featurewise_std_normalization=False,
    	rotation_range=20,
    	width_shift_range=0.2,
    	height_shift_range=0.2,
    	horizontal_flip=False)

		datagen.fit(self.X_train)

		# fits the model on batches with real-time data augmentation:
		self.model.fit_generator(datagen.flow(self.X_train, self.Y_train, batch_size=128),
                    samples_per_epoch=len(self.X_train), nb_epoch=1)


		self.model.save_weights(filepath)
		loss_and_metrics = self.model.evaluate(self.X_test, self.Y_test, batch_size=128)
		print loss_and_metrics

