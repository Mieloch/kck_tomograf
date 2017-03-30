from math import floor, sqrt, ceil
import numpy as np


class WorkingSpace:
    def __init__(self, source_img):
        self.source_img = source_img
        self.source_w = source_img.shape[0]
        self.source_h = source_img.shape[1]
        self.working_space = self.__create_working_space(source_img)
        self.w = self.working_space.shape[0]
        self.h = self.working_space.shape[1]

    def source_x_y(self):
        return int((self.w - self.source_w) / 2), int((self.h - self.source_h) / 2)

    def source_d(self):
        return ceil(sqrt(self.source_w ** 2 + self.source_h ** 2))

    def center_x_y(self):
        return int(self.w / 2), int(self.h / 2)

    def __create_working_space(self, source_img):
        background_size = self.calculate_background_size()
        working_space = self.__create_img_with_background(background_size, source_img)
        return working_space

    def calculate_background_size(self):
        img_diameter = self.source_d()
        background_size = img_diameter * 2
        if background_size % 2 != 0:
            background_size += 1
        return background_size

    def __create_img_with_background(self, background_size, source_img):
        img_with_background = np.zeros((background_size, background_size))
        img_with_background[:, :] = 0
        h_ = (background_size - self.source_h) / 2
        w_ = (background_size - self.source_w) / 2
        img_with_background[h_:h_ + self.source_h, w_:w_ + self.source_w] = source_img
        return img_with_background
