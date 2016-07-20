import numpy as np
import os
from model import *


# from tests import *

# path to load the training checkpoint
this_dir, this_filename = os.path.split(__file__)
filepath = os.path.join(os.path.dirname(this_dir), 'data', 'weights.best.conv2.hdf5')

model = default_model


def predict(pixels):

    model.load_weights(filepath)

    pixels_input = np.asarray(pixels)
    # visualize(pixels_input)

    pixels_input = pixels_input.reshape(1, 1, 28, 28)
    # visualize(pixels_input[0][0])

    predicted = model.predict(pixels_input, verbose = 1)
    print predicted

    imax = 0

    for i in range(10):

        if predicted[0][i] > predicted[0][imax]:

            imax = i

    print "The number is " + str(imax)
