import skimage.io as io

def load_img(name):
    data_img = io.imread(name, as_grey=True)
    if data_img.max() > 1:
        data_img = data_img / 255
    return data_img

def save_reconstruct(img):
    io.imsave("output/reconstruct.png", img)

def save_sinogram(img):
    io.imsave("output/sinogram.png", img)

def save_img(img, path):
    io.imsave(path, img)

def save_scans(results):
    for i, result in enumerate(results):
        io.imsave("output/scans/" + str(i) + ".png", result)