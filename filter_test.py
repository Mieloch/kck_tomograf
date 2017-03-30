import util
import filter
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize


def filter_sinogram_test():
    sinogram = util.load_img("output/sinogram.png")
    filtered_sinogram = filter.filter_sinogram(sinogram)
    util.save_img(filtered_sinogram, "output/filtered_sinogram.png")





def main():
    sinogram = util.load_img("output/sinogram.png")

    column = sinogram[:, 150]
    plt.subplot(311)
    plt.plot(column)
    plt.subplot(312)
    mask = filter.ramp2(10)
    plt.plot(mask)
    plt.subplot(313)
    conv = np.convolve(mask, column, mode="same")
    plt.plot(conv)
    plt.show()

main();
# filter_sinogram_test()
