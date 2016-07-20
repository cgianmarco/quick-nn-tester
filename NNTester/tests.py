import Image
import numpy as np
import ImageFilter


def visualize(array):
    array_visual = np.copy(array).astype(np.uint8)
    for i in range(len(array_visual)):
        for j in range(len(array_visual)):
            array_visual[i][j] = array_visual[i][j] * 255
    im = Image.fromarray(array_visual)

    # im = im.convert('I')
    # im = im.filter(ImageFilter.GaussianBlur)
    im.show()

def visualize_filter(array):
    array_visual = np.copy(array).astype(np.uint8)
    for i in range(len(array_visual)):
        for j in range(len(array_visual)):
            array_visual[i][j] = array_visual[i][j] * 255
    im = Image.fromarray(array_visual)

    # im = im.convert('I')
    im = im.filter(ImageFilter.Kernel((3,3), filter))
    im.show()