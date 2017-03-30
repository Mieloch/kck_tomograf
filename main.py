import util
from tomograph import Tomograph


def main():
    emiters_count = None;
    input = util.load_img("input/wiki.png")

    tomograph = Tomograph(input, emiters_count)
    sinogram = tomograph.get_sinogram()
    util.save_sinogram(sinogram)
    reconstruct = tomograph.get_reconstruct()
    util.save_reconstruct(reconstruct)

    print("END")


main()
